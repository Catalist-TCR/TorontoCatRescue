import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPE = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_name(
    'google.auth', SCOPE)


def find_permission(user):
    gcon = gspread.authorize(CREDENTIALS)
    wks = gcon.open("users").sheet1
    all_rows = wks.get_all_values()
    user_emails = [item[0] for item in all_rows]
    user_permissions = [item[1] for item in all_rows]

    try:
        user_index = user_emails.index(user)
    except ValueError:
        user_index = -1

    if user_index >= 0:
        return user_permissions[user_index]
    return ""


def input_data(form, permission):
    print(repr(form))
    print(form)
    gcon = gspread.authorize(CREDENTIALS)
    wks = gcon.open("Catalist").sheet1
    index = len(wks.get_all_values()) + 1
    wks.update_cell(index, 1, form.date.data.strftime("%B %d, %Y"))
    wks.update_cell(index, 2, form.name.data)
    wks.update_cell(index, 3, form.date_of_birth.data.strftime("%B %d, %Y"))
    wks.update_cell(index, 4, form.age.data)
    wks.update_cell(index, 5, form.sex.data)
    wks.update_cell(index, 6, form.description.data)
    wks.update_cell(index, 7, form.sn.data)
    wks.update_cell(index, 8, form.shelter_name.data)
    wks.update_cell(index, 9, form.shelter_id.data)
    #wks.update_cell(index, 10, form.photo.data)
    wks.update_cell(index, 10, form.fiv_tested.data)
    wks.update_cell(index, 11, form.flv_tested.data)
    wks.update_cell(
        index, 12, form.fvrcp_vaccination_date.data.strftime("%B %d, %Y"))
    wks.update_cell(
        index, 13, form.rabies_vaccination_date.data.strftime("%B %d, %Y"))
    wks.update_cell(index, 14, form.medical_notes.data)
    #wks.update_cell(index, 16, form.medical_documents.data)
    wks.update_cell(index, 15, form.behaviour_notes.data)
    wks.update_cell(index, 16, form.urgent.data)
    wks.update_cell(index, 17, form.petpoint_id.data)
    wks.update_cell(index, 18, form.outcome.data)
    if form.intake_date.data is not None:
        wks.update_cell(index, 19, form.intake_date.data.strftime("%B %d, %Y"))
    if form.foster_placement_date.data is not None:
        wks.update_cell(
            index, 20, form.foster_placement_date.data.strftime("%B %d, %Y"))
    wks.update_cell(index, 21, form.location.data)
    if permission == 'foster':
        wks.update_cell(index, 22, 'foster')
    elif permission == 'shelter':
        wks.update_cell(index, 22, 'shelter')
    elif permission == 'intake':
        wks.update_cell(index, 22, 'intake')
    wks.update_cell(index, 23, form.foster_coordinator.data)
    wks.update_cell(index, 24, form.foster_parent.data)


def return_database():
    gcon = gspread.authorize(CREDENTIALS)
    wks = gcon.open("Catalist").sheet1
    return wks.get_all_values()
