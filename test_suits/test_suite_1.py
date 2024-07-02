# Test Suit 1: Checking if there are no tasks when a new user visits the page
from playwright.sync_api import expect
from datetime import datetime
import calendar


def test_site_has_current_day(set_up):
    page = set_up
    main_title = page.get_by_role("heading")
    current_date = datetime.today()
    today = calendar.day_name[current_date.weekday()]
    expect(main_title).to_contain_text(f"Happy {today}")


def test_homepage(set_up):
    page = set_up
    paragraph = page.get_by_role("paragraph")
    expect(paragraph).to_contain_text("Please, add a new task.")


def test_active_tasks_page(set_up):
    page = set_up
    page.get_by_role("link", name="Active").click()
    paragraph = page.get_by_role("paragraph")
    expect(paragraph).to_contain_text("There are no active tasks currently.")


def test_completed_tasks_page(set_up):
    page = set_up
    page.get_by_role("link", name="Completed").click()
    paragraph = page.get_by_role("paragraph")
    page.screenshot()
    expect(paragraph).to_contain_text("There are no completed tasks currently.")
