from src.utils.utils import *


def details_controller():
    """
    Controller for the details page.
    """
    account = RotateAccounts(accounts)
    next_account = account.nextAccount()

    api = getLinkedin(next_account["user"], next_account["password"])

    data = api.get_profile('insira um perfil do linkedin aqui...')
    save_to_json(data, 'profile')
    
    info = api.get_profile_posts(data["profile_id"])
    save_to_json(info, 'posts')

    network = api.get_profile_network_info(data["profile_id"])
    save_to_json(network, 'network')

    badge = api.get_profile_member_badges(data["profile_id"])
    save_to_json(badge, 'badges')

    updates = api.get_profile_updates(data["profile_id"])
    save_to_json(updates, 'updates')
