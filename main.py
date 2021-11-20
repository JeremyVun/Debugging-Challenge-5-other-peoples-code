from argparse import ArgumentParser
from bs4 import BeautifulSoup
import time, requests, re

"""
Wiki Crawler

Task:
This program starts at the wikipedia page you give it and keeps following the first wikipedia link it finds until it reaches the Philosophy Wikipedia page.

Unfortunately, someone has sabotaged the code base. It is up to you to fix it.
"""

# This is used to find links in the page
regex = re.compile("^/wiki/[A-Za-z1-10_% ]*$")

# The wikipedia website
baseUrl = "https://en.wikipedia.org"

def main():
  start_topic = "Main_Page"
  end_topic = "Philosophy"

  try:
    print(f"Starting at {baseUrl}/wiki/{start_topic}")
    result, trace = crawl(start_topic)

    # print the results of the program
    number_of_steps = len(trace)
    if result:
      success_text = f"[Success] {number_of_step} steps"
    else:
      success_text = f"[Failure] {number_of_step} steps"
    
    print(success_text)

    # If you pass this test, you have succeeded!
    assert success_text == "[Success] 24 steps", "Program was not succesful in 25 steps"

  except Exception as e:
    print(f"ERROR: {e}")


def crawl(start_topic, end_topic):
  links_seen = {}
  trace_history = []
  next_link = start_topic

  while (next_link):
    req_start = time.time()

    # Fetch the wikipedia page
    wikipedia_page = f"{baseUrl}/wiki/{next_link}"
    src = requests.get(wikipedia_page).text

    # Record that we have been to this link
    links_seen[next_link] = True

    # We are using "BeautifulSoup" and "lxml" to
    # help us parse the wikipedia html
    soup = BeautifulSoup(src, "lxml")
    
    current_topic = soup.title.string.replace(" - Wikipedia", "")
    trace_history.append(current_topic)

    # Check if we reached the "Philosophy" page yet
    if current_topic == end_topic
      req_end = time.time()
      time_taken = int((req_end-req_start)*1000)
      print(f"Wiki: {current_topic} - ({time_taken}ms)")
      return False, tracehistory

    next_link = get_next_link(soup.body, links_seen)

    req_end = time.time()
    time_taken = int((req_end-req_start)*1000)
    print(f"Wiki: {current_topic} - ({time_taken}ms)")

  return True, tracehistory


def get_next_link(body, links_seen):
  # for every paragraph in the wikipedia,
  # find the first link that we haven't visited yet
  for p in body.find_all('p'):

    # Iterate through all the links in the page
    for link in p.find_all('a', href=regex):
      link_topic = link["href"].split("/")[-1]

      # Let's make sure we don't visit the same wikipedia page more than once
      if link_topic not in links_seen:
        return link_topic

  return None


if __name__ == "__main__":
  main()