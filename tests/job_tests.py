from src.utils.utils import RotateAccounts
from factory import getLinkedin
from config.account import accounts


account = RotateAccounts(accounts)
next_account = account.nextAccount()
api = getLinkedin(next_account["user"], next_account["password"])
jobs = api.search_jobs(companies="")
