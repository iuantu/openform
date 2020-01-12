from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
    JSON,
)
from .mixins import TimeStampMixin

class UserAgentMixin:

    ip = Column(String(15), nullable=True)
    ua_browser = Column(String(100), nullable=True)
    ua_browser_version = Column(String(10), nullable=True)
    ua_os = Column(String(100), nullable=True)
    ua_os_version = Column(String(10), nullable=True)
    ua_device = Column(String(50), nullable=True)
    ua_device_brand = Column(String(50), nullable=True)
    ua_device_model = Column(String(50), nullable=True)

    def assemble_from_user_agent(self, user_agent):
        self.ip = user_agent.ip
        self.ua_browser = user_agent.browser
        self.ua_browser_version = user_agent.browser_version
        self.ua_os = user_agent.os
        self.ua_os_version = user_agent.os_version
        self.ua_device = user_agent.device
        self.ua_device_brand = user_agent.device_brand
        self.ua_device_model = user_agent.device_model

class UserAgent:
    def __init__(self, ip, browser, browser_version, os, os_version, device,
        device_brand, device_model):

        self.ip = ip
        self.browser = browser
        self.browser_version = browser_version
        self.os = os
        self.os_version = os_version
        self.device = device
        self.device_brand = device_brand
        self.device_model = device_model