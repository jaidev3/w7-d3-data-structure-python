from collections import deque

class BrowserHistory:
    def __init__(self, max_size=5):
        self.max_size = max_size
        self.history = deque(maxlen=max_size)
        self.forward_stack = deque()

    def add_page(self, url):
        self.history.append(url)
        self.forward_stack.clear()  # Clear forward stack on new page
        self.print_state()

    def go_back(self):
        if len(self.history) > 1:
            self.forward_stack.append(self.history.pop())
            self.print_state()
        else:
            print("Cannot go back: at the oldest page")
            self.print_state()

    def go_forward(self):
        if self.forward_stack:
            self.history.append(self.forward_stack.pop())
            self.print_state()
        else:
            print("Cannot go forward: no pages in forward stack")
            self.print_state()

    def print_state(self):
        print(f"History: {list(self.history)}")
        print(f"Forward Stack: {list(self.forward_stack)}")

# Example usage
if __name__ == "__main__":
    browser = BrowserHistory()
    
    # Add pages
    browser.add_page("page1.com")
    browser.add_page("page2.com")
    browser.add_page("page3.com")
    browser.add_page("page4.com")
    browser.add_page("page5.com")
    browser.add_page("page6.com")  # Should remove page1.com
    
    # Go back twice
    browser.go_back()
    browser.go_back()
    
    # Go forward once
    browser.go_forward()
    
    # Add new page
    browser.add_page("page7.com")


#test