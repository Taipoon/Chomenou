import sys

from PyQt6.QtCharts import QChart, QChartView, QBarSeries, QBarSet, QValueAxis, QBarCategoryAxis
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

from domain.entities import Statement, Account
from domain.helpers.metaclass_resolver import make_cls
from domain.shared import Config
from domain.views import StatisticsView
from presenters.statistics_presenter import StatisticsPresenter

BAR_CHART_TICK_INTERVAL = 5000
BAR_CHART_MINOR_TICK_COUNT = 3


class StatisticsWindow(QWidget, StatisticsView, metaclass=make_cls()):
    def __init__(self, current_year: int):
        super().__init__()
        self._global_layout = None
        self._presenter = StatisticsPresenter(self)
        self._current_year = current_year

    def initialize_ui(self):
        self.setGeometry(200, 200, 1200, 900)
        self.setWindowTitle("統計情報")
        self._global_layout = QVBoxLayout()

        update_button = QPushButton("更新")
        update_button.clicked.connect(self._update_accounts_summary)
        self._global_layout.addWidget(update_button)

        self.setLayout(self._global_layout)

    def _update_accounts_summary(self):
        self._presenter.update_accounts_summary(year=self._current_year)

    def update_accounts_summary_bar_chart(self, summary: dict[Account: list[Statement]]):
        """
        棒グラフで勘定科目別のサマリを表示します
        :param summary: サマリデータ
        :return: None
        """
        # グラフの作成
        chart = QChart()
        chart.setTitle(f"{self._current_year}年度 勘定科目別 集計")
        chart.legend().setVisible(False)

        # X軸(勘定科目名をカテゴリとして設定)
        account_name_category_x_axis = QBarCategoryAxis()
        # Y軸(金額)
        amount_value_y_axis = QValueAxis()

        # 棒グラフのシリーズを作成
        series = QBarSeries()
        # 棒グラフを作成
        bar_set = QBarSet("")

        max_value = 0
        for account, statement in summary.items():
            # カテゴリの追加
            account_name_category_x_axis.append(account.name)

            if statement is None:
                bar_set.append(0)
            else:
                v = statement.amount.value
                if v > max_value:
                    max_value = v
                bar_set.append(float(statement.amount.value))

            series.append(bar_set)

        # グラフに棒をセット
        chart.addSeries(series)

        # X軸の設定
        chart.addAxis(account_name_category_x_axis, Qt.AlignmentFlag.AlignBottom)
        series.attachAxis(account_name_category_x_axis)

        # Y軸の設定
        # キリの良いY軸の最大値を求める
        max_value = calculate_max_range_value(max_value)
        amount_value_y_axis.setRange(0, max_value)
        # Y軸ラベルの表示方法
        amount_value_y_axis.setLabelFormat("%d")
        # 小目盛りの数
        amount_value_y_axis.setMinorTickCount(BAR_CHART_MINOR_TICK_COUNT)
        # 目盛りの数と間隔の設定
        amount_value_y_axis.setTickInterval(BAR_CHART_TICK_INTERVAL)
        amount_value_y_axis.setTickCount(max_value // (BAR_CHART_TICK_INTERVAL * 2))
        # 軸の設置
        chart.addAxis(amount_value_y_axis, Qt.AlignmentFlag.AlignLeft)
        series.attachAxis(amount_value_y_axis)

        # グラフ描画のアニメーションとテーマを設定
        chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
        chart.setTheme(QChart.ChartTheme.ChartThemeBrownSand)

        # グラフを描画するエリアを作成してウィンドウに設置
        chart_view = QChartView()
        chart_view.setChart(chart)
        self._global_layout.addWidget(chart_view)


def calculate_max_range_value(max_value: int):
    s = str(max_value)
    # 桁数
    c = len(s)
    # 最上位の桁
    u = int(s[0])
    return (u + 1) * 10 ** (c - 1)


if __name__ == '__main__':
    Config.parse()
    app = QApplication(sys.argv)
    dialog = StatisticsWindow(2025)
    dialog.show()
    sys.exit(app.exec())
