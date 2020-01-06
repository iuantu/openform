from user_agents import parse
from app.models import UserAgent

def to_user_agent(request):
    ua = parse(request.user_agent.string)
                
    user_agent = UserAgent(
        request.remote_addr,
        ua.browser.family,
        ua.browser.version_string,
        ua.os.family,
        ua.os.version_string,
        ua.device.family,
        ua.device.brand,
        ua.device.model
    )

    return user_agent