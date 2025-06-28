import customtkinter as ctk
from PIL import Image

class ClientFrame(ctk.CTkFrame):
    frame_count = 0

    def __init__(self, main, title):
        super().__init__(main)
        self.title = title
        ClientFrame.frame_count += 1
        
        self.geometry("300x300")

        # client image
        self.client_image = ctk.CTkImage(dark_image=Image.open("./esp32.png"), size=(30, 30))
        self.client_image.grid(row=1, column=ClientFrame.frame_count - 1, padx=10, pady=(10, 0))
        self.client_image_label = ctk.CTkLabel(main, image=self.client_image, text=self.title)
        self.client_image_label.grid(row=0, column=ClientFrame.frame_count - 1, padx=10, pady=(10, 0))

        # status label
        self.status_label = ctk.CTkLabel(main, text="Status: ", text_color="white")
        self.status_label.grid(row=2, column=ClientFrame.frame_count - 1, padx=10, pady=(10, 0))
        self.status_value_label = ctk.CTkLabel(main, text="Unknown", text_color="grey")
        self.status_value_label.grid(row=2, column=ClientFrame.frame_count - 1, padx=(0, 10), pady=(10, 0))

        # checkhealth button
        self.checkhealth_button = ctk.CTkButton(main, text="CheckHealth", command=self.checkhealth_button_callback)
        self.checkhealth_button.grid(row=3, column=ClientFrame.frame_count - 1, padx=10, pady=(10, 0))

        # tts textbox and send button
        self.tts_textbox = ctk.CTkTextbox(main, width=250, corner_radius=10)
        self.tts_textbox.grid(row=4, column=ClientFrame.frame_count - 1, padx=10, pady=(10, 0))
        self.send_tts_button = ctk.CTkButton(main, text="Send TTS", command=self.send_tts_button)
        self.send_tts_button.grid(row=5, column=ClientFrame.frame_count - 1, padx=10, pady=(10, 0))

        # tts toggle
        self.tts_toggle_var = ctk.StringVar(value="on")
        self.tts_toggle = ctk.CTkSwitch(main, text="Toggle TTS", command=self.tts_toggle_callback, 
                                        variable=self.tts_toggle_var, onvalue="on", offvalue="off")
        self.tts_toggle.grid(row=6, column=ClientFrame.frame_count - 1, padx=10, pady=(10, 0))

        # current count label
        self.count_label = ctk.CTkLabel(main, text="Count: ", text_color="white")
        self.count_label.grid(row=7, column=ClientFrame.frame_count - 1, padx=10, pady=(10, 0))
        self.count_value_label = ctk.CTkLabel(main, text="0", text_color="grey")
        self.count_value_label.grid(row=7, column=ClientFrame.frame_count - 1, padx=(0, 10), pady=(10, 0))

    def checkhealth_button_callback(self):
        print("Check Health Button Pressed")

    def send_tts_button_callback(self):
        print("Send TTS Button Pressed!")

    def tts_toggle_callback(self):
        print("TTS Toggle Toggled!", self.tts_toggle.get())

    def test_tts_button_callback(self):
        print("Test TTS Button Pressed!")

    def configure_status_value_label(self):
        self.status_value_label.configure(text="Successfully Configured!", text_color="green")

    def configure_count_value_label(self):
        self.count_value_label.configure(text="+1", text_color="green")


class Server(ctk.CTk):
    def __init__(self, server_name, client_names):
        super().__init__()
        self.server_name = server_name
        self.client_names = client_names

        self.clients = []

        self.geometry("640x640")

        for i, client in enumerate(client_names):        
            client_frame = ClientFrame(self, client)
            client_frame.grid(row=0, column=i, padx=10, pady=(10, 0), sticky="w")

            client_frame.configure_status_value_label()
            client_frame.configure_count_value_label()


ctk.set_appearance_mode("dark")
gui = Server(server_name="Door Greeter Server", client_names=["EntranceESP", "ExitESP"])

gui.mainloop()