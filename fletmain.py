import flet as ft
import datetime
import pandas as pd

df = pd.read_csv('PV-Data-22tm24.csv')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


start1 = "04/02/2024 00:00"
end2 = "04/02/2024 23:59"

todo_check_value = False
energy = False


def main(page: ft.Page):
    start = "Empty"
    end = "Empty"

    output_text = ft.Text()

    def on_dialog_result(e: ft.FilePickerResultEvent):
        print("Selected files:", e.files)
        print("Selected file or directory:", e.path)
        print(file_picker.path.value)

    file_picker = ft.FilePicker(on_result=on_dialog_result)
    page.overlay.append(file_picker)

    filebutton = ft.ElevatedButton("Choose files...",
                      on_click=lambda _: file_picker.pick_files(allow_multiple=True))
    def checkbox_changed(e):
        if todo_check_value == True:
            energy = True

        elif todo_check_value == False:
            energy = False
        page.update()

    page.title = "Solar Data Reading"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def change_date2(e):
        print(f"Date picker changed, value is {range_picker_to.value}")

    def date_picker_dismissed2(e):
        print(f"Date picker dismissed, value is {range_picker_to.value}")

    range_picker_to = ft.DatePicker(
        on_change=change_date2,
        on_dismiss=date_picker_dismissed2,
        first_date=datetime.datetime(2023, 10, 1),
        last_date=datetime.datetime(2024, 10, 1),
    )

    page.overlay.append(range_picker_to)

    range_picker_to_button = ft.ElevatedButton(
        "Pick date",
        icon=ft.icons.CALENDAR_MONTH,
        on_click=lambda _: range_picker_to.pick_date(),
    )

    def range_picker_from_change_date(e):
        print(f"Date picker changed, value is {range_picker_from.value}")

    def range_picker_from_dismissed(e):
        print(f"Date picker dismissed, value is {range_picker_from.value}")

    def calculate2(e):
        if range_picker_from.value == None:
            show_banner_click(True)
            return True
        elif range_picker_to.value == None:
            show_banner_click(True)
            return False
        else:
            result = df[(df['Date/Time'] >= str(datetime.datetime.strptime(str(range_picker_from.value), '%Y-%m-%d %H:%M:%S').strftime('%m/%d/%Y %H:%M'))) & (df['Date/Time'] <= str(datetime.datetime.strptime(str(range_picker_to.value), '%Y-%m-%d %H:%M:%S').strftime('%m/%d/%Y %H:%M')))],
            results = result,
            print(results),
            lv.controls.append(ft.Text(results)),
            page.update()

    def close_banner(e):
        page.banner.open = False
        page.update()


    page.banner = ft.Banner(
        bgcolor=ft.colors.LIGHT_BLUE_ACCENT_700,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.LIGHT_BLUE_ACCENT_100, size=40),
        content=ft.Text(
            "Oops, a date value is empty, ensure you have selected a date correctly."
        ),
        actions=[
            ft.TextButton("Close", on_click=close_banner),
        ],
    )

    data_1 = [
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(1, 1),
                ft.LineChartDataPoint(3, 1.5),
                ft.LineChartDataPoint(5, 1.4),
                ft.LineChartDataPoint(7, 3.4),
                ft.LineChartDataPoint(10, 2),
                ft.LineChartDataPoint(12, 2.2),
                ft.LineChartDataPoint(13, 1.8),
            ],
            stroke_width=8,
            color=ft.colors.LIGHT_GREEN,
            curved=True,
            stroke_cap_round=True,
        ),
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(1, 1),
                ft.LineChartDataPoint(3, 2.8),
                ft.LineChartDataPoint(7, 1.2),
                ft.LineChartDataPoint(10, 2.8),
                ft.LineChartDataPoint(12, 2.6),
                ft.LineChartDataPoint(13, 3.9),
            ],
            color=ft.colors.PINK,
            below_line_bgcolor=ft.colors.with_opacity(0, ft.colors.PINK),
            stroke_width=8,
            curved=True,
            stroke_cap_round=True,
        ),
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(1, 2.8),
                ft.LineChartDataPoint(3, 1.9),
                ft.LineChartDataPoint(6, 3),
                ft.LineChartDataPoint(10, 1.3),
                ft.LineChartDataPoint(13, 2.5),
            ],
            color=ft.colors.CYAN,
            stroke_width=8,
            curved=True,
            stroke_cap_round=True,
        ),
    ]

    chart = ft.LineChart(
        data_series=data_1,
        border=ft.Border(
            bottom=ft.BorderSide(4, ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE))
        ),
        left_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=1,
                    label=ft.Text("1m", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=2,
                    label=ft.Text("2m", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=3,
                    label=ft.Text("3m", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=4,
                    label=ft.Text("4m", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=5,
                    label=ft.Text("5m", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=6,
                    label=ft.Text("6m", size=14, weight=ft.FontWeight.BOLD),
                ),
            ],
            labels_size=40,
        ),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=2,
                    label=ft.Container(
                        ft.Text(
                            "SEP",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                ft.ChartAxisLabel(
                    value=7,
                    label=ft.Container(
                        ft.Text(
                            "OCT",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                ft.ChartAxisLabel(
                    value=12,
                    label=ft.Container(
                        ft.Text(
                            "DEC",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
            ],
            labels_size=32,
        ),
        tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY),
        min_y=0,
        max_y=4,
        min_x=0,
        max_x=14,
        # animate=5000,
        expand=True,
    )
    def show_banner_click(e):
        page.banner.open = True
        page.update()

    lv = ft.ListView(spacing=10, padding=20, height=300)
    range_picker_from = ft.DatePicker(
        on_change=range_picker_from_change_date,
        on_dismiss=range_picker_from_dismissed,
        first_date=datetime.datetime(2000, 1, 1),
        field_hint_text="dd/mm/yyyy"

    )

    page.overlay.append(range_picker_from)

    range_picker_from_button = ft.ElevatedButton(
        "Pick date",
        icon=ft.icons.CALENDAR_MONTH,
        on_click=lambda _: range_picker_from.pick_date(),
    )

    page.add(
        ft.Row(
            [
                ft.Checkbox(label="Check for energy readings instead of time", value=False, on_change=checkbox_changed)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.Text("From", size=20),
                range_picker_from_button
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.Text("    To", size=20),
                range_picker_to_button
            ],
            alignment=ft.MainAxisAlignment.CENTER,

        ),
        ft.Row(
            [
                ft.ElevatedButton("Calculate", icon="calculate", on_click=calculate2),
                filebutton
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                lv
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                chart

            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(target=main)
