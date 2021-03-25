import requests
import xlsxwriter
import sys

def main():
    base_url = "https://reqres.in/api/"
    req_list_users = "users?page=2"

    url_req_list_users = base_url+req_list_users

    try:
        get_list_users = requests.get(url = url_req_list_users)
        response = get_list_users.status_code
    except requests.exceptions.Timeout:
        print ("Retries to be implemented")
        # exit for now
        return 1
    except requests.exceptions.RequestException as e:
        print ("Exception: Exception occured. Exiting...")
        print (e)
        return 1

    if response == 404:
        print ("Error: User or resources not found")
        return 1

    json_list_users = get_list_users.json()
    create_excel = create_excel_sheet(json_list_users)

    if 0 != create_excel:
        return 1

    return 0


def create_excel_sheet(json_list_users):
    # Create an new Excel file and add a worksheet.
    try:
        workbook = xlsxwriter.Workbook('user_data.xlsx')
        worksheet = workbook.add_worksheet()
    except xlsxwriter.exceptions.FileCreateError as e:
        print ("Exception: File user_data.xlsx creation failed, check if the file is not already open")
        return 1

    # Widen the columns to make the text clearer.
    worksheet.set_column('A:A', 15)
    worksheet.set_column('B:B', 15)
    worksheet.set_column('C:C', 30)

    # Title row
    worksheet.write('A1', 'Last Name')
    worksheet.write('B1', 'First Name')
    worksheet.write('C1', 'Email')

    row_count = 2
    for root in json_list_users:
        # print (root)
        if root == "data":
            user_data = json_list_users["data"]
            for profile in user_data:
                #print (profile)
                worksheet.write('A'+str(row_count), profile['last_name'])
                worksheet.write('B' + str(row_count), profile['first_name'])
                worksheet.write('C' + str(row_count), profile['email'])
                row_count += 1

    workbook.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())