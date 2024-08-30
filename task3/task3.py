import json
import sys


def fill_values(tests, values_dict):
    for test in tests:
        if 'id' in test and test['id'] in values_dict:
            test['value'] = values_dict[test['id']]

        if 'values' in test:
            fill_values(test['values'], values_dict)


def main(tests_file, values_file, report_file):
    try:
        with open(values_file, 'r') as vf:
            values_data = json.load(vf)

        with open(tests_file, 'r') as tf:
            tests_data = json.load(tf)

        values_dict = {item['id']: item['value'] for item in values_data['values']}

        fill_values(tests_data['tests'], values_dict)

        with open(report_file, 'w') as rf:
            json.dump(tests_data, rf, indent=4)

    except FileNotFoundError as e:
        print(f"Файл не найден - {e.filename}")
    except json.JSONDecodeError as e:
        print(f"Некорректный формат JSON в файле - {e}")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    else:
        tests_file = sys.argv[1]
        values_file = sys.argv[2]
        report_file = sys.argv[3]

        main(tests_file, values_file, report_file)