# autopep8: off
import asyncio
import customtkinter as ctk
import tkinter as tk
import logging
import os

from datetime import datetime
from tkinter import messagebox
from typing import Self, Tuple

from PIL import Image, ImageTk
from playwright.async_api import Page

from src.utils.globals.get_app_path import get_app_path
from src.utils.globals.html_generator import html_generator
from src.utils.sites.linkedin import Linkedin
from src.utils.sites.post_image import PostImage
from src.utils.sites.spotfy import Spotfy
from src.types.ui.html_data import HtmlData
from src.utils.browsers.browser_playwright import BrowserPlaywright
from src.utils.browsers.engines import Engines

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):

    def __init__(self: Self, loop: asyncio.AbstractEventLoop):
        super().__init__()

        self.path_storage = get_app_path(2, "/data/sessions/linkedin.json")

        self.browser = BrowserPlaywright()
        self.page = None

        self.loop = loop
        self.start()

        self.title("ALT+TAB Soundtrack")
        self.geometry("1100x750")

        self.grid_columnconfigure(0, weight=6)
        self.grid_columnconfigure(1, weight=4)
        self.grid_rowconfigure(1, weight=1)
        self.after(100, lambda: self.state("zoomed"))

        self.create_top()
        self.create_form()
        self.create_preview()

        self.link_album = None


    def start(self: Self):
        self.execute_async(
            self.create_page(),
        )


    async def create_page(self: Self) -> Page:
        self.page = await self.browser.create_page(Engines.MSEDGE, self.path_storage)


    def create_top(self: Self):
        frame = ctk.CTkFrame(self)
        frame.grid(row=0, column=0, columnspan=2,
                   sticky="ew", padx=10, pady=10)

        app_name = ctk.CTkLabel(
            frame,
            text="🎧 ALT+TAB Soundtrack",
            font=("Segoe UI", 20, "bold")
        )
        app_name.pack(side="left", padx=20, pady=10)

    def create_form(self: Self):

        frame = ctk.CTkScrollableFrame(self)
        frame.grid(row=1, column=0, sticky="nsew",
                   padx=10, pady=10)

        ctk.CTkLabel(frame, text="Link do Spotify").pack(anchor="w")

        self.link_spotify = ctk.CTkEntry(frame, width=500)
        self.link_spotify.insert(0, "https://open.spotify.com/intl-pt/track/57iDDD9N9tTWe75x6qhStw")
        self.link_spotify.pack(fill="x")

        ctk.CTkLabel(frame, text="Número da edição").pack(anchor="w")

        self.edition_number = ctk.CTkEntry(frame)
        self.edition_number.insert(0, "003")
        self.edition_number.pack(fill="x")

        # song_frame
        song_frame = ctk.CTkFrame(frame)
        song_frame.pack(fill="x", pady=10)

        # Faz as duas colunas ocuparem 50% cada
        song_frame.grid_columnconfigure(0, weight=1)
        song_frame.grid_columnconfigure(1, weight=1)

        # Coluna 1
        ctk.CTkLabel(song_frame, text="Título").grid(row=0, column=0, sticky="w")

        self.music_title = ctk.CTkEntry(song_frame)
        self.music_title.grid(row=1, column=0, sticky="ew", padx=(0, 5))

        # Coluna 2
        ctk.CTkLabel(song_frame, text="Artista").grid(row=0, column=1, sticky="w")

        self.muscic_artist = ctk.CTkEntry(song_frame)
        self.muscic_artist.grid(row=1, column=1, sticky="ew", padx=(5, 0))
        # song_frame

        # situation_frame
        situation_frame = ctk.CTkFrame(frame)
        situation_frame.pack(fill="x", pady=10)

        situation_frame.grid_columnconfigure(0, weight=2)
        situation_frame.grid_columnconfigure(1, weight=8)

        # Coluna 1
        ctk.CTkLabel(situation_frame, text="Título da situação ->") \
            .grid(row=0, column=0, sticky="w")

        # Coluna 2
        self.situation_title = ctk.CTkComboBox(
            situation_frame,
            values=[
                "Você está no trabalho e, de repente...",
            ],
            # command=mudou
        )
        self.situation_title.grid(row=0, column=1, sticky="ew", padx=(5, 0))

        self.situation = ctk.CTkTextbox(frame, height=80)
        self.situation.insert(0.0, "Consegue resolver um problema ... e aparecem outros três.")
        self.situation.pack(fill="x")
        # situation_frame


        # curiosity_frame
        curiosity_frame = ctk.CTkFrame(frame)
        curiosity_frame.pack(fill="x", pady=10)

        curiosity_frame.grid_columnconfigure(0, weight=2)
        curiosity_frame.grid_columnconfigure(1, weight=8)

        # Coluna 1
        ctk.CTkLabel(curiosity_frame, text="Título da curiosidade ->").grid(row=0, column=0, sticky="w")

        # Coluna 2
        self.curiosity_title = ctk.CTkComboBox(
            curiosity_frame,
            values=[
                "Curiosidade",
            ],
            # command=mudou
        )
        self.curiosity_title.grid(row=0, column=1, sticky="ew", padx=(5, 0))

        self.curiosity = ctk.CTkTextbox(frame, height=80)
        self.curiosity.insert(0.0, '"Bitter Sweet Symphony" ficou marcada pelo final do filme Segundas Intenções e transmite exatamente essa sensação: algumas vitórias vêm acompanhadas de novos desafios.')
        self.curiosity.pack(fill="x")
        # curiosity_frame

        # question_frame
        question_frame = ctk.CTkFrame(frame)
        question_frame.pack(fill="x", pady=10)

        question_frame.grid_columnconfigure(0, weight=2)
        question_frame.grid_columnconfigure(1, weight=8)

        # Coluna 1
        ctk.CTkLabel(question_frame, text="Título da pergunta ->").grid(row=0, column=0, sticky="w")

        # Coluna 2
        self.question_title = ctk.CTkComboBox(
            question_frame,
            values=[
                "E para você?",
            ],
            # command=mudou
        )
        self.question_title.grid(row=0, column=1, sticky="ew", padx=(5, 0))

        self.question = ctk.CTkTextbox(frame, height=80)
        self.question.insert(0.0, "Qual música faz você pensar que finalmente deu tudo certo... até abrir o próximo e-mail?")
        self.question.pack(fill="x", pady=(0, 20))
        # question_frame

        # post_date_frame
        entry_frame = ctk.CTkEntry(frame, placeholder_text="DD/MM/AAAA")
        entry_frame.pack(padx=20, pady=20)

        def validar():
            texto = entry_frame.get()
            try:
                datetime.strptime(texto, "%d/%m/%Y")
                print("Data válida")
            except ValueError:
                print("Data inválida")

        botao = ctk.CTkButton(frame, text="Validar", command=validar)
        botao.pack()
        # post_date_frame

        buttons = ctk.CTkFrame(frame)
        buttons.pack(fill="x")

        self.button_start = ctk.CTkButton(
            buttons,
            text="Gerar HTML",
            command=self.run_process
        )
        self.button_start.pack(side="left", padx=5)

        self.button_post_linkedin = ctk.CTkButton(
            buttons,
            text="Postar Linkedin",
            command=self.run_post_linkedin
        )
        self.button_post_linkedin.pack(side="left", padx=5)


    def clear_preview(self):
        self.preview_canvas.delete("all")
        self.preview_photo = None


    def create_preview(self):
        self.preview_frame = ctk.CTkFrame(self)
        self.preview_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
        self.preview_frame.grid_rowconfigure(1, weight=1)
        self.preview_frame.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(
            self.preview_frame,
            text="Preview da imagem"
        ).grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.preview_canvas = tk.Canvas(
            self.preview_frame,
            highlightthickness=0,
            bd=0,
            bg="#2b2b2b"  # ou outra cor
        )
        self.preview_canvas.grid(row=1, column=0, sticky="nsew")


    def execute_async(self: Self, coroutine, on_success=None, on_error=None):
        future = asyncio.run_coroutine_threadsafe(
                coroutine,
                self.loop
            )
        def callback(future):
            try:
                result = future.result()
                if on_success:
                    self.after(
                        0,
                        lambda: on_success(result)
                    )
            except Exception as e:
                if on_error:
                    self.after(
                        0,
                        lambda: on_error(e)
                    )
        future.add_done_callback(callback)


    async def create_html(self: Self):
        data: HtmlData = {
            "link_spotify": self.link_spotify.get(),
            "edition_number": self.edition_number.get(),
            "music_title": self.music_title.get(),
            "muscic_artist": self.muscic_artist.get(),
            "link_album": self.link_album,
            "situation_title": self.situation_title.get(),
            "situation": self.situation.get("0.0", "end"),
            "curiosity_title": self.curiosity_title.get(),
            "curiosity": self.curiosity.get("0.0", "end"),
            "question_title": self.question_title.get(),
            "question": self.question.get("0.0", "end")
        }
        file_path = await html_generator(data)
        logging.info("HTML gerado: %s", file_path)


    def run_process(self):
        self.execute_async(
            self.process(),
        )

    def run_post_linkedin(self: Self):
        self.execute_async(
            self.post_linkedin(),
        )

    async def process(self: Self):
        self.clear_preview()

        self.edit_button_label("disabled", "Buscando Spotify...")
        link = self.link_spotify.get()
        data = await self.get_spotify(link)
        self.update_spotify(data)

        self.edit_button_label("disabled", "Criando html...")
        await self.create_html()

        self.edit_button_label("disabled", "Tirando print da tela...")
        await self.get_image()

        self.edit_button_label("disabled", "Mostrando imagem...")
        await self.update_preview("post.png")

        self.edit_button_label("enabled", "Gerar HTML")
        messagebox.showinfo("Sucesso", "Operação concluída!")


    async def get_spotify(self, link) -> Tuple[str, str, str]:
        spotify = Spotfy(self.page)
        await spotify.go_to_page(link)
        title = await spotify.get_music_title()
        artist = await spotify.get_music_artist()
        link_album = await spotify.get_link_album()
        return title, artist, link_album


    def update_spotify(self, data):
        music_title, muscic_artist, link_album = data
        self.link_album = link_album
        self.music_title.delete(0, "end")
        self.music_title.insert(0, music_title)
        self.muscic_artist.delete(0, "end")
        self.muscic_artist.insert(0, muscic_artist)


    def edit_button_label(self: Self, state: str, text: str):
        self.button_start.configure(
            state=state,
            text=text
        )


    async def get_image(self: Self):
        link = get_app_path(2, "/output/post.html")
        image = PostImage(self.page)
        await image.go_to_page(link.resolve().as_uri())
        path = get_app_path(2, "/output/post.png")
        await image.get_screenshot(path)


    async def update_preview(self, file_name: str):
        relative_path = f"/output/{file_name}"
        path = get_app_path(2, relative_path)
        image = Image.open(path)
        self.preview_canvas.update_idletasks()
        frame_w = self.preview_canvas.winfo_width()
        frame_h = self.preview_canvas.winfo_height()
        ratio = min(
            frame_w / image.width,
            frame_h / image.height
        )
        new_size = (
            int(image.width * ratio),
            int(image.height * ratio)
        )
        image = image.resize(new_size, Image.Resampling.LANCZOS)
        self.preview_photo = ImageTk.PhotoImage(image)
        self.preview_canvas.delete("all")
        self.preview_canvas.create_image(
            frame_w // 2,
            frame_h // 2,
            image=self.preview_photo,
            anchor="center"
        )


    async def post_linkedin(self: Self):
        link = "https://www.linkedin.com/"
        linkedin = Linkedin(self.page)
        path = get_app_path(2, "/output/post.png")

        if os.path.exists(path):

            await linkedin.go_to_page(link, wait_time=15)

            if not await linkedin.is_logged(os.getenv("LINKEDIN_NAME")):
                await linkedin.insert_email(os.getenv("LINKEDIN_USER"))
                await linkedin.insert_password(os.getenv("LINKEDIN_PASSWORD"))
                await linkedin.click_access()
                await asyncio.sleep(30)
                await self.browser.save_storage(self.path_storage)

            await linkedin.send_image(path)
        else:
            messagebox.showerror ("Erro", "Arquivo não criado para postagem.")
