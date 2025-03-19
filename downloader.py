import tkinter.ttk
import customtkinter
import tkinter
from tkinter import ttk # To build the table of downloads.
from PIL import Image, ImageTk
from tkinter import filedialog
import os




# System settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# App Frame
app = customtkinter.CTk()
app.geometry("800x400")
app.title("Sigma Download Manager")

# Logo Display
app.iconbitmap('C:/users/USER/Desktop/VSCODE/Python/Assets/sigmadarkmodelogo.ico')


# ---- BEGIN NORMAL DOWNLOADS POPUP ----



def add_download_popup():
    global url, file_name, save_path
    # Create a new Toplevel window
    popup = tkinter.Toplevel(app, bg='#0A0D0F')
    popup.title("Add Download")
    # Remove window decorations (title bar, minimize/maximize buttons)
    # popup.overrideredirect(True)
    popup.resizable(False, False)  # Disable Minimize and Maximize buttons 

    # Logo Display
    popup.iconbitmap("C:/users/USER/Desktop/VSCODE/Python/Assets/sigmadarkmodelogo.ico")

    # Set the size and position of the popup
    popup_width = 720
    popup_height = 380
    x = app.winfo_x() + (app.winfo_width() // 2) - (popup_width // 2)
    y = app.winfo_y() + (app.winfo_height() // 2) - (popup_height // 2)
    popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

    # PopUp Frame
    entire_popup_frame = tkinter.Frame(popup, width=430, height=220, background='#1C2026')
    entire_popup_frame.pack(fill='both', expand=True)

    # PopUp Title and Cancel Button Frame
    popup_main_frame = tkinter.Frame(entire_popup_frame, width=720, height=50, background='#0A0D0F')
    popup_main_frame.pack(padx=2, pady=2, side=tkinter.TOP)

    # Enter URL label/Title
    popup_title = tkinter.Label(popup_main_frame, width=10, background='#0A0D0F', foreground='white', text="Enter URL", font=('bold', 16))
    popup_title.place(x=10, y=8)

    # Function to Automate FilePath Choice
    def choose_save_path():                             # REMEMBER TO CREATE A BUTTON TO CALL THIS FUNCTION. CHOOSE PATH BUTTON
        global save_path
        selected_path = filedialog.askdirectory()       # Opens a dialog to choose directory
        if selected_path:
            save_path = selected_path
 
# URL Entry
    url_var = tkinter.StringVar()
    url_entry = customtkinter.CTkEntry(entire_popup_frame, placeholder_text='Enter/ Paste File Link', 
                                       width=460, height=35, border_width=1, textvariable=url_var)
    url_entry.place(x=8, y=100)
    #collecting the url
    def download_file():
        url = url_var.get()
        print(f"collected URL: {url}")
        if url:
            import subprocess
            subprocess.Popen(["aria2c", url])

# PopUp Add and Cancel Buttons
    # File Save Path, Add and Cancel Buttons Frame
    popup_buttons_frame = tkinter.Frame(entire_popup_frame,  width=720, height=30, background='#1C2026')
    popup_buttons_frame.place(x=1, y=300)

    # Choose File Save Path Button
    file_save_path_button = customtkinter.CTkButton(popup_buttons_frame, text="Browse", corner_radius=4, height=30, width=50, font=('bold', 16), text_color='yellow', fg_color='transparent', command=choose_save_path)
    file_save_path_button.pack(padx=75, pady=4, side=tkinter.LEFT)

    # Add button
    add_button = customtkinter.CTkButton(popup_buttons_frame, text="Download", corner_radius=4, height=30, width=100, font=('bold', 16), text_color='white', fg_color='yellow', border_width=1, command=download_file)
    add_button.pack(padx=20, pady=4, side=tkinter.RIGHT)

    # Cancel button
    cancel_button = customtkinter.CTkButton(popup_buttons_frame, text="Close", corner_radius=4, height=30, width=100, font=('bold', 16), text_color='white', fg_color='transparent', border_width=1, command=popup.destroy)
    cancel_button.pack(padx=5, pady=4, side=tkinter.RIGHT)

# ---- END NORMAL DOWNLOAD POPUP ----





# ---- BEGIN YOUTUBE POPUP CODE ---- 

# Add Download PopUp
def yt_download_popup():
    # Create a new Toplevel window
    yt_popup = tkinter.Toplevel(app, bg='#333333')
    yt_popup.title("Add Download")
    # Remove window decorations (title bar, minimize/maximize buttons)
    # yt_popup.overrideredirect(True)
    yt_popup.resizable(False, False)

    # Logo Display
    yt_popup.iconbitmap("C:/users/USER/Desktop/VSCODE/Python/Assets/sigmadarkmodelogo.ico")

    # Set the size and position of the popup
    yt_popup_width = 800
    yt_popup_height = 800
    x = app.winfo_x() + (app.winfo_width() // 2) - (yt_popup_width // 2)
    y = app.winfo_y() + (app.winfo_height() // 2) - (yt_popup_height // 2)
    yt_popup.geometry(f"{yt_popup_width}x{yt_popup_height}+{x}+{y}")

    # PopUp Frame
    yt_entire_popup_frame = tkinter.Frame(yt_popup, width=430, height=220, background='#1C2026')
    yt_entire_popup_frame.pack(fill='both', expand=True)

    # PopUp Title Frame
    yt_popup_main_frame = tkinter.Frame(yt_entire_popup_frame, width=800, height=50, background='#0A0D0F')
    yt_popup_main_frame.pack(padx=2, pady=2, side=tkinter.TOP)

    # Enter URL label/Title
    yt_popup_title = tkinter.Label(yt_popup_main_frame, width=10, background='#0A0D0F', foreground='white', text="YouTube", font=('bold', 16))
    yt_popup_title.place(x=10, y=8)

# ---- Resolution options and File Save Path ----

    #  ---- URL Entry Label ----
    yt_url_entry_label = tkinter.Label(yt_entire_popup_frame, background='#1C2026', 
                                         foreground='white', font=('bold', 18), 
                                         text='Paste Video Link') 
    yt_url_entry_label.place(x=10, y=80)
    
    yt_url_entry_frame = tkinter.LabelFrame(yt_entire_popup_frame, background='#1C2026', 
                                              width=780, height=80)
    yt_url_entry_frame.pack(padx=5, pady=90)

    # Entry widget
    yt_url_entry = customtkinter.CTkEntry(yt_url_entry_frame, placeholder_text='Paste YouTube Video Link', width=510, height=30, 
                                          border_width=1)
    yt_url_entry.place(x=4, y=10)


    # ---Resolution Label ---
    yt_resolutions_label = tkinter.Label(yt_entire_popup_frame, background='#1C2026', 
                                         foreground='white', font=('bold', 18), 
                                         text='Choose Resolution') 
    yt_resolutions_label.place(x=300, y=250)

    yt_resolutions_frame = tkinter.LabelFrame(yt_entire_popup_frame, background='#1C2026', 
                                              width=500, height=200)
    yt_resolutions_frame.pack(padx=5, pady=10)

# ---- Resolutions Radio Buttons ----

    # Create a variable to hold the radio button selection
    radio_var = customtkinter.StringVar()

        # Function to handle the selection
    def show_selection():
        selected_option = radio_var.get()                   # -- Remember to take this variable and add it to ydl-opts dictionary(ies)
        print(f"Selected Option: {selected_option}")

    # Create radio buttons
    radio_button1 = customtkinter.CTkRadioButton(yt_resolutions_frame, text="1080p, MP4 H264 - AAC - 50fps", font=('bold', 14), variable=radio_var, value="Option 1", command=show_selection, radiobutton_width=15, radiobutton_height=15) # Set the Values == to quality dictionaries.
    radio_button2 = customtkinter.CTkRadioButton(yt_resolutions_frame, text="720p, MP4 H264 - AAC - 50fps", font=('bold', 14), variable=radio_var, value="Option 2", command=show_selection, radiobutton_width=15, radiobutton_height=15)
    radio_button3 = customtkinter.CTkRadioButton(yt_resolutions_frame, text="480p, MP4 H264 - AAC - 25fps", font=('bold', 14), variable=radio_var, value="Option 3", command=show_selection, radiobutton_width=15, radiobutton_height=15)
    radio_button4 = customtkinter.CTkRadioButton(yt_resolutions_frame, text="360p, MP4 VP9 - AAC - 25fps", font=('bold', 14), variable=radio_var, value="Option 4", command=show_selection, radiobutton_width=15, radiobutton_height=15)

    # Pack the radio buttons into the dropdown frame
    radio_button1.pack(anchor='w', padx=45, pady = 8)
    radio_button2.pack(anchor='w', padx=45, pady = 8)
    radio_button3.pack(anchor='w', padx=45, pady = 8)
    radio_button4.pack(anchor='w', padx=45, pady = 8)

# ---- End of Resolution Code ----

# ---- Begin File Path Code ----
    
    def browse_file():
        # Open file dialog to select a directory
        filepath = filedialog.askdirectory()  # Use askopenfilename() for files
        if filepath:
            yt_file_path_entry.delete(0, customtkinter.END)  # Clear the entry field
            yt_file_path_entry.insert(0, filepath)  # Insert the chosen path

    def download():
        """Placeholder function for download logic."""
        # Add your download logic here
        # You can access selected options and file path from the widgets
        print("Download button clicked!")

    # --- File Save Path ---
    yt_file_path_frame = tkinter.LabelFrame(yt_entire_popup_frame, background='#1C2026', foreground='white', text="File Save Path", font=('bold', 16), width=700, height=100, padx=10, pady=35)
    yt_file_path_frame.pack()

    yt_file_path_entry = customtkinter.CTkEntry(yt_file_path_frame, width=250, height=30, border_width=1)
    yt_file_path_entry.pack(side=tkinter.LEFT)

    yt_browse_button = customtkinter.CTkButton(yt_file_path_frame, text="Browse", corner_radius=4, height=30, width=100, font=('bold', 16), text_color='yellow', fg_color='#0094FF', command=browse_file)
    yt_browse_button.pack(padx= 5, side=tkinter.LEFT)

    # --- Buttons ---
    yt_button_frame = tkinter.Frame(yt_entire_popup_frame, width=700, height=100, pady=20, background='#1C2026')
    yt_button_frame.pack(padx=50, side=tkinter.RIGHT)

    yt_cancel_button = customtkinter.CTkButton(yt_button_frame, text="Close", corner_radius=4, height=30, width=100, font=('bold', 16), text_color='white', border_width=1, fg_color='transparent',command=yt_popup.destroy)
    yt_cancel_button.pack(side=tkinter.LEFT, padx=5)

    yt_download_button = customtkinter.CTkButton(yt_button_frame, text="Download", corner_radius=4, height=30, width=100, font=('bold', 16), text_color='white', fg_color='#0094FF',command=download)
    yt_download_button.pack(side=tkinter.LEFT, padx=5)

# ---- END YOUTUBE POPUP CODE ----


# App UI
# Menu Frame
menu_frame = tkinter.Frame(app, width=900, height=60, background='#333333') # Change BG color//Use Hex
menu_frame.pack(padx=2, pady=2, fill='x', side = tkinter.TOP)

# Menu Items/Buttons
add_button = tkinter.Button(menu_frame, text='New', font=('bold', 17), fg = '#e1f4e7', bd=0, bg='#333333', command=add_download_popup)
add_button.place(x=10, y=8)

pause_button = tkinter.Button(menu_frame, text ="Pause", font=('bold', 17), fg = '#e1f4e7', bd=0, bg='#333333', )
pause_button.place(x=87, y=8)

resume_button = tkinter.Button(menu_frame, text ="Resume", font=('bold', 17), fg = '#e1f4e7', bd=0, bg='#333333', )
resume_button.place(x=188, y=8)

delete_button = tkinter.Button(menu_frame, text ="Delete", font=('bold', 17), fg = '#e1f4e7', bd=0, bg='#333333', )
delete_button.place(x=308, y=8)

# YOUTUBE DOWNLOAD BUTTON
yt_download_button = customtkinter.CTkButton(menu_frame, text='YouTube', corner_radius=4, font=('bold', 17), text_color='red', fg_color='transparent', hover_color='#292929', border_width=1, command=yt_download_popup)
yt_download_button.pack(padx=20, pady=8, fill='x', side=tkinter.RIGHT)



# Main Frame to house Treeeview
main_frame = tkinter.Frame(app, width=900, height=855, background='#292929') # Change BG color// Use Hex
main_frame.pack(padx=2, pady=2, fill='both', expand=True, side = tkinter.TOP)

# New Tree View for Downloads List.
# Create a style for the Treeview
style = ttk.Style()
style.theme_use('clam')  # Use clam theme as a base

# Configure the Treeview style
style.configure("Treeview",
                background="#292929",  # Dark background
                foreground="#FFFFFF",  # White text
                rowheight=25,
                fieldbackground="#292929", # Same as background
                font=('bold', 16))          # Downloads list font size

# Configure the selected item color
style.map("Treeview",
          background=[("selected", "#3C3C3C")],  # Darker background when selected (Alt Color #0094ff)
          foreground=[("selected", "#FFFFFF")])  # White text when selected

# Set row height
style.configure("Treeview", rowheight=60)  # Increase row height

# Set font for the headings
style.configure("Treeview.Heading", 
                background="#292929", 
                foreground="#FFFFFF", 
                font=('bold', 17))

# Configure the style of headings
style.map("Treeview.Heading",
          background=[("selected", "#3C3C3C")],  # Darker background when selected
          foreground=[("selected", "#FFFFFF")])  # White text when selected

# Create the TreeView
tree = ttk.Treeview(main_frame, style="Treeview")
tree["columns"] = ("File Size", "Download Speed", "Progress")

# Define columns with custom sizes
tree.column("#0", width=200)  # File Name
tree.column("File Size", width=100)  # File Size
tree.column("Download Speed", width=120)  # Download Speed
tree.column("Progress", width=80)  # Progress

# Set headings with increased font size
tree.heading("#0", text="File Name", anchor='w')
tree.heading("File Size", text="File Size", anchor='w')
tree.heading("Download Speed", text="Download Speed", anchor='w')
tree.heading("Progress", text="Progress", anchor='w')








    
# Run App
app.mainloop()


