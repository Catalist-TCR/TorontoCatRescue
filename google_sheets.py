import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('google.auth', scope)

gc = gspread.authorize(credentials)

#sh = gc.create('users')
#sh.share('illariojane@gmail.com', perm_type='user', role='writer')



wks = gc.open("users").sheet1
row_list = wks.get_all_values()
print(len(row_list))
print(wks)

#wks.update_acell('B2', "it's down there somewhere, let me take another look.")

# Fetch a cell range
#cell_list = wks.range('A1:B7')