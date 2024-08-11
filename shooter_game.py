import pandas as pd
df = pd.read_csv('GooglePlayStore_wild.csv')
"""# Виведи інформацію про весь DataFrame, щоб дізнатися, які стовпці потребують очищення
print(df.info())
# Скільки в датасеті додатків, у яких не вказано (NaN) рейтинг (Rating)?
print(len(df[pd.isnull(df['Rating'])]))
# Заміни порожнього значення ('NaN') рейтингу ('Rating') для таких програм на -1.
df['Rating'].fillna(-1, inplace = True)"""




# Визнач, яке значення розміру ('Size') зберігається в датасеті крім Кілобайтів і Мегабайтів, заміни його на -1.
# Перетвори розміри додатків ('Size') у числовий формат (float). Розмір усіх програм повинен вимірюватися в Мегабайтах.
print(df['Size'].value_counts())
def set_size(size):
   if size[-1] == 'M':
      return float(size[:-1])
   elif size[-1] == 'k':
      return float(size[:-1]) / 1024
   return -1
df['Size'] = df['Size'].apply(set_size)


# Чому дорівнює максимальний розмір ('Size') додатків із категорії ('Category') 'TOOLS'?
print(df[df['Category'] == 'TOOLS']['Size'].max())









"""
#Бонусні завдання
# Заміни тип даних на цілий (int) для кількості установок ('Installs').
# У записі кількості установок ('Installs') знак "+" необхідно ігнорувати.
# Тобто. якщо в датасеті кількість установок дорівнює 1,000,000+, необхідно змінити значення на 1000000


def set_installs(installs):
   if installs == '0':
       return 0
   return int(installs[:-1].replace(',', ''))
df['Installs'] = df['Installs'].apply(set_installs)


# Згрупуй дані за типом ('Type') та цільовою аудиторією ('Content Rating') будь-яким зручним для тебе способом,
# Порахуй середню кількість установок ('Installs') у кожній групі. Результат округлили до десятих.
# В отриманій таблиці знайди комірку з найбільшим значенням.
# До якої вікової групи та типу додатків відносяться дані з цієї комірки?


print(round(df.pivot_table(index = 'Content Rating', columns = 'Type', values = 'Installs', aggfunc = 'mean')), 1)


# Яка програма не вказує тип ('Type')? Який тип необхідно записати в залежності від ціни?
print(df[pd.isnull(df['Type'])])
#Щоб побачити всі стовпці замість крапки, можна застосувати iloc[0].
# print(df[pd.isnull(df['Type'])].iloc[0])
df['Type'].fillna('Free', inplace = True)


#Виведи інформацію про весь DataFrame, щоб переконатися, що очищення пройшло успішно
print(df.info())"""
