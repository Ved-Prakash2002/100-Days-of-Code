import tkinter as tk  # Import the tkinter library for GUI creation.
import time  # Import the time module to track user activity.

class EphemeralEditor:
    """
    A simple text editor with a built-in timeout feature.
    Clears the text area after a specified period of user inactivity.
    """
    def __init__(self, master, timeout=5):
        """
        Initializes the EphemeralEditor instance.

        Parameters:
        - master: The root Tkinter window.
        - timeout: Time (in seconds) of inactivity before clearing the text area (default is 5 seconds).
        """
        self.master = master  # Reference to the root Tkinter window.
        master.title("Ephemeral Text Editor")  # Set the window title.

        # Create a text area widget for user input.
        self.text_area = tk.Text(master, wrap=tk.WORD)  # Word wrap enabled for the text area.
        self.text_area.pack(expand=True, fill="both")  # Make the text area fill the window.

        self.timeout = timeout  # Set the timeout duration for inactivity.
        self.last_activity_time = time.time()  # Track the last time the user typed.
        self.timer_id = None  # Initialize the timer ID for managing the inactivity timer.

        # Bind a key release event to the text area to reset the inactivity timer on user input.
        self.text_area.bind("<KeyRelease>", self.reset_timer)

    def reset_timer(self, event=None):
        """
        Resets the inactivity timer whenever the user types in the text area.

        Parameters:
        - event: The event object passed by the key release binding (default is None).
        """
        self.last_activity_time = time.time()  # Update the last activity time to the current time.

        # Cancel any existing timer to avoid overlapping checks.
        if self.timer_id:
            self.master.after_cancel(self.timer_id)

        # Set a new timer to check for inactivity after the specified timeout.
        self.timer_id = self.master.after(int(self.timeout * 1000), self.check_inactivity)

    def check_inactivity(self):
        """
        Checks if the user has been inactive for the specified timeout duration.
        If inactive, clears the text area.
        """
        # Compare the current time with the last activity time.
        if time.time() - self.last_activity_time > self.timeout:
            self.text_area.delete("1.0", tk.END)  # Clear all text in the text area.

        # Schedule the next inactivity check.
        self.timer_id = self.master.after(int(self.timeout * 1000), self.check_inactivity)


# Main Tkinter application setup.
root = tk.Tk()  # Create the root window.
editor = EphemeralEditor(root)  # Initialize the EphemeralEditor with the root window.
root.mainloop()  # Start the Tkinter event loop to keep the application running.
