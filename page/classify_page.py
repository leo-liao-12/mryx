# -*- coding: utf-8 -*-
# @Time : 2020/10/18 15:26
# @Author : leo
# @Email : oldbigdo@foxmail.com
# @File : classify_page.py
# @Project : mryx
from appium.webdriver.common.mobileby import MobileBy as By
from page.base_page import BasePage

"""我的页面"""
class ClassifyPage(BasePage):

    """定位器"""

    """搜索框"""
    search_text_loc = (By.ID,"cn.missfresh.application:id/tv_search_text")

    """点击后搜索框搜索框"""
    search_view_loc = (By.XPATH,"//android.widget.EditText[@resource-id=\"cn.missfresh.application:id/search_view\"]")

    """搜索物品recycler"""
    result_recycler_loc = (By.ID,"cn.missfresh.application:id/result_recycler")

    """搜索后购物车"""
    cart_view_loc = (By.XPATH, "//android.widget.ImageView[@resource-id=\"cn.missfresh.application:id/cart_view\"]")

    """牛奶特仑苏"""
    suggest_contentt_loc = (By.ANDROID_UIAUTOMATOR,"new UiSelector().className(\"android.widget.TextView\")."
                                                   "textContains(\"牛奶特仑苏\").resourceId(\"cn.missfresh.application:id/suggestContent\")")