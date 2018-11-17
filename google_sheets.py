import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('google.auth', scope)

gc = gspread.authorize(credentials)

#sh = gc.create('users')
#sh.share('illariojane@gmail.com', perm_type='user', role='writer')

def find_permission(user):

	wks = gc.open("users").sheet1
	all_rows = wks.get_all_values()
	user_emails = [item[0] for item in all_rows]
	user_permissions = [item[1] for item in all_rows]
	
	try:
		user_index = user_emails.index(user)
	except ValueError:
		user_index = -1

	if user_index >= 0:
		#print(user_index, user_permissions[user_index])
		return user_permissions[user_index]

	#wks.update_acell('B2', "it's down there somewhere, let me take another look.")

	# Fetch a cell range
	#cell_list = wks.range('A1:B7')

if __name__ == '__main__':
	user = raw_input()
	find_permission(user)