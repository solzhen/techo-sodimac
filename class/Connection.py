import gspread
from oauth2client.service_account import ServiceAccountCredentials

class Connection:

	def __init__(self, document, keyfile):
		scope = ['https://spreadsheets.google.com/feeds']
		creds = ServiceAccountCredentials.from_json_keyfile_name(keyfile, scope)
		client = gspread.authorize(creds)

		self.sheet = client.open(document)

	def get_sheet1(self):
		return self.sheet.sheet1

