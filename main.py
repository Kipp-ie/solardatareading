import flet as ft
import datetime
import pandas as pd

df = pd.read_csv('PV-Data-22tm24.csv')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
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
        end = str(datetime.datetime.strptime(str(date_picker2.value), '%Y-%m-%d %H:%M:%S').strftime('%m/%d/%Y %H:%M'))
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
        start = str(datetime.datetime.strptime(str(date_picker.value), '%Y-%m-%d %H:%M:%S').strftime('%m/%d/%Y %H:%M'))
        print(f"Date picker changed, value is {start}")

    def date_picker_dismissed(e):
        print(f"Date picker dismissed, value is {date_picker.value}")

    def calculate2(e):
        print(start)
        print(end)
        result = df[(df['Date/Time'] >= str(datetime.datetime.strptime(str(date_picker.value), '%Y-%m-%d %H:%M:%S').strftime('%m/%d/%Y %H:%M'))) & (df['Date/Time'] <= str(datetime.datetime.strptime(str(date_picker2.value), '%Y-%m-%d %H:%M:%S').strftime('%m/%d/%Y %H:%M')))]
        print(result)

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
        )
    )


ft.app(target=main)