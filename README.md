# Evaluating future salary

This program fetches programming vacancies for the most popular programming languages through HeadHunter and SuperJob API and calculates average salary by programming language. Results are presented in form of a table.

### How to install

Python3 should already be installed. Use pip (or pip3, in case of conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
To get data through SuperJob API you will need a secret key. [Register an app](https://api.superjob.ru/register) in order to get one. After that, create an `.env` file in the project directory and put your secret key in the `SUPERJOB_SECRET_KEY` variable:
```
SUPERJOB_SECRET_KEY = 'YOUR_SECRET_KEY'
```

### Usage

To run the program use the following command from the project directory:
```
python main.py
```
Example of the result:
```
+HeadHunter Moscow------+------------------+---------------------+------------------+
| Язык программирования | Вакансий найдено | Вакансий обработано | Средняя зарплата |
+-----------------------+------------------+---------------------+------------------+
| JavaScript            | 2836             | 744                 | 177551           |
| Java                  | 2157             | 321                 | 206716           |
| Python                | 2208             | 446                 | 192785           |
| Ruby                  | 156              | 40                  | 193275           |
| PHP                   | 1240             | 547                 | 169746           |
| C++                   | 1154             | 324                 | 175818           |
| C#                    | 1123             | 270                 | 179751           |
| 1C                    | 2880             | 970                 | 158608           |
| Swift                 | 355              | 84                  | 235291           |
+-----------------------+------------------+---------------------+------------------+
+SuperJob Moscow--------+------------------+---------------------+------------------+
| Язык программирования | Вакансий найдено | Вакансий обработано | Средняя зарплата |
+-----------------------+------------------+---------------------+------------------+
| JavaScript            | 38               | 22                  | 130250           |
| Java                  | 9                | 4                   | 231000           |
| Python                | 25               | 17                  | 160555           |
| Ruby                  | 4                | 2                   | 264500           |
| PHP                   | 21               | 16                  | 159577           |
| C++                   | 17               | 9                   | 145666           |
| C#                    | 6                | 4                   | 210000           |
| 1C                    | 50               | 39                  | 161474           |
| Swift                 | 4                | 2                   | 187500           |
+-----------------------+------------------+---------------------+------------------+
```
Also,  scripts could be run separately:
```
python headhunter_parser.py

python superjob_parser.py
```
Such run will print vacancies dictionary to console

### Project Goals

The code is written for educational purposes on online-course for web-developers [Devman](https://dvmn.org).