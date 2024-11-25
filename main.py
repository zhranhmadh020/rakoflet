from flet import *
import datetime

def main(page: Page):
    page.window.width = 330
    page.window.height = 740
    page.window.top = 1
    page.window.left = 1050
    page.theme_mode = ThemeMode.DARK
    page.scroll = "auto"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = MainAxisAlignment.CENTER

    page.appbar = AppBar(
        bgcolor=colors.AMBER,
        title=Text("مرحباً بحامي الوطن"),
        center_title=True,
        leading=Icon(icons.HOME),
        leading_width=40
    )
    a = Stack([
        Column([
            Text(
                "اهلا بك عزيزي المستخدم",
                color=colors.WHITE,
                size=25,
                width=330,
                rtl="true",
                weight="bold",
                opacity=0.8),
            Text(
                "ادخل الموعد النهائي (اخرك يوم ايه)",
                color=colors.WHITE,
                size=20,
                width=330,
                rtl="true",
                weight="bold",
                opacity=0.8),
        ]),
    ])
  
    dayin=TextField(label="يوم",
                  helper_text="اخر يوم",
                  color=colors.BLUE_50,
                  bgcolor=colors.BLACK45,
                  icon=icons.TODAY,
                  width=110,
                  height=60,
                  
                  )
    monthin=TextField(label="شهر",
                  helper_text="اخر شهر",
                  color=colors.BLUE_50,
                  bgcolor=colors.BLACK45,
                  width=80,
                  height=60,
                  
                  )
    yearin=TextField(label="سنة",
                  helper_text="اخر سنة",
                  color=colors.BLUE_50,
                  bgcolor=colors.BLACK45,
                  width=80,
                  height=60,
                  
                  )
    inputs=Row(controls=[dayin,monthin,yearin],alignment=MainAxisAlignment.CENTER)
      #فانكشن الحساب
    def calculate(e):
        now = datetime.date.today()
         # تحويل القيم المدخلة إلى أعداد صحيحة
        day = int(dayin.value)
        month = int(monthin.value)
        year = int(yearin.value)
        future = datetime.date(year=year, month=month, day=day)
        remaining_day = (future - now).days
        years = remaining_day // 365
        remaining_day %= 365
        months = remaining_day // 30
        remaining_day %= 30
        # تحديث النص ليظهر المدة المتبقية
        n.value = f"المدة المتبقية: {years} سنة، {months} شهر، {remaining_day} يوم"
        page.update()  # تحديث الصفحة لعرض النتيجة
        
    f = ElevatedButton(text="احسب باقي كام يوم ",
                       bgcolor=colors.BLUE,
                       width=230,
                       height=60,
                       icon=icons.SUMMARIZE,
                       icon_color="green300",
                       on_click=calculate
                       )

    n = Text("المدة المتبقية:", size=30, bgcolor="red",)

    page.update()
    page.add(a, inputs, Column([f, n],alignment=alignment.center, rtl=True))

app(main)
