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

    def checkbox_changed(e):
        if todo_check_value == True:
            energy = True

        elif todo_check_value == False:
            energy = False
        page.update()

    page.title = "Solar Data Reading"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def change_date2(e):
        print(f"Date picker changed, value is {end}")

    def date_picker_dismissed2(e):
        print(f"Date picker dismissed, value is {date_picker2.value}")

    date_picker2 = ft.DatePicker(
        on_change=change_date2,
        on_dismiss=date_picker_dismissed2,
        first_date=datetime.datetime(2023, 10, 1),
        last_date=datetime.datetime(2024, 10, 1),
    )

    page.overlay.append(date_picker2)

    date_button2 = ft.ElevatedButton(
        "Pick date",
        icon=ft.icons.CALENDAR_MONTH,
        on_click=lambda _: date_picker2.pick_date(),
    )

    def change_date(e):
        print(f"Date picker changed, value is {start}")

    def date_picker_dismissed(e):
        print(f"Date picker dismissed, value is {date_picker.value}")

    def calculate2(e):
        if date_picker.value == None:
            show_banner_click(True)
            return True
        elif date_picker2.value == None:
            show_banner_click(True)
            return False
        else:
            result = df[(df['Date/Time'] >= str(datetime.datetime.strptime(str(date_picker.value), '%Y-%m-%d %H:%M:%S').strftime('%m/%d/%Y %H:%M'))) & (df['Date/Time'] <= str(datetime.datetime.strptime(str(date_picker2.value), '%Y-%m-%d %H:%M:%S').strftime('%m/%d/%Y %H:%M')))],
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

    def show_banner_click(e):
        page.banner.open = True
        page.update()

    lv = ft.ListView(spacing=10, padding=20, height=300)
    date_picker = ft.DatePicker(
        on_change=change_date,
        on_dismiss=date_picker_dismissed,
        first_date=datetime.datetime(2000, 1, 1),
        field_hint_text="dd/mm/yyyy"

    )

    page.overlay.append(date_picker)

    date_button = ft.ElevatedButton(
        "Pick date",
        icon=ft.icons.CALENDAR_MONTH,
        on_click=lambda _: date_picker.pick_date(),

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
                date_button
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.Text("    To", size=20),
                date_button2
            ],
            alignment=ft.MainAxisAlignment.CENTER,

        ),
        ft.Row(
            [
                ft.ElevatedButton("Calculate", icon="calculate", on_click=calculate2),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                lv
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )


ft.app(target=main)
