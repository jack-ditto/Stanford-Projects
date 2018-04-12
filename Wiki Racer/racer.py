import re
import queue
import requests
from queue import PriorityQueue

def parse_child_links(text):
	''' Parse wikipedia links from page '''
	links_reg = re.compile(r'href="/wiki/([0-9a-zA-Z_%-]+)"')
	return [m for m in links_reg.findall(text)]
	
def get_page_text(link_name):
	''' Get text from wikipedia page '''
	base_url = 'https://en.wikipedia.org/wiki/'
	return requests.get(base_url+link_name).text
	
def get_priority(link_name, end_page_links):
	''' Get num of shared links btwn page and target page '''
	page_text = get_page_text(link_name)
	links = parse_child_links(page_text)
	len(set(links)&set(end_page_links))
	return len(set(links)&set(end_page_links))
	
def Main():
	''' Main function '''
	# Initialize queue
	q = queue.PriorityQueue()		# Priority queue object
	start_page = ['Milkshake']	# Defining start and end pages
	end_page = ['Gene']
	q.put((0, start_page))			# Put empty ladder in to queue
	print("Finding path from %s to %s..." % (start_page[0], end_page[0]))
	
	# Get links on end page
	end_page_text = get_page_text(end_page[0])
	end_links = parse_child_links(end_page_text)
	
	# Initialize visited links list
	visited = list()
	
	# Keep going until end found or no more elements
	while not q.empty():
		dequed = q.get()
		ladder = dequed[1]
		visited.append(ladder[-1])
		page_text = get_page_text(ladder[-1])
		child_links = parse_child_links(page_text)
		print("Trying path: %s" % " -> ".join(str(x) for x in ladder))
		
		# Check if solution is found
		if end_page[0] in child_links:
			ladder.append(end_page[0])
			print("Page found! Ladder: %s" % " -> ".join(str(x) for x in ladder))
			return None
			
		# Cycle through links on page
		for l in child_links:
			
			# Add link to queue if not visited
			if l not in visited:
				new_ladder = ladder[:]		
				new_ladder.append(l)
				q.put((-get_priority(l, end_links), new_ladder))
	
if __name__ == "__main__":
	Main()


