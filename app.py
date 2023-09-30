import streamlit as st
import PIL.Image
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import jinja2
import pdfkit
import base64
import os
import subprocess, platform
import base64
from fpdf import FPDF


my_name="Jorge O."
item1="Cosa 1"


context = {'my_name': my_name, 'item1': item1}

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

html_template = 'template.html'
template = template_env.get_template(html_template)
output_text = template.render(context)



st.set_page_config(
    page_title="Herramientas AI - Qüid Lab",
    page_icon="random",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Oculto botones de Streamlit
#hide_streamlit_style = """
#				<style>
#				#MainMenu {visibility: hidden;}
#
#				footer {visibility: hidden;}
#				</style>
#				"""
#st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Funciones


def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'



# Logo sidebar
image = PIL.Image.open('logo_blanco.png')
st.sidebar.image(image, width=None, use_column_width=None)

with st.sidebar:
    selected = option_menu(
        menu_title="Selecciona",  # required
        options=["Home", "Texto", "Audio", "Otras", "Créditos"],  # required
        icons=["house", "caret-right-fill", "caret-right-fill","caret-right-fill",
                        "caret-right-fill", "envelope"],  # optional
        menu_icon="upc-scan",  # optional
        default_index=0,  # optional
    )




if selected == "Home":
	st.title("Experimenta con IA - Listado de herramientas externas")
	st.write("En este listado hemos recopilado algunas herramientas que pueden ser de utilidad para la generación de imágenes y texto por medio de IA.\n \n Recuerda que siempre tienes que revisar y validar cualquier respuesta que obtengas de una herramienta IA.\n\n\n\n")
	st.write(' ')
	st.write("**Instrucciones:** \n ")
	"""
* Selecciona "Imagenes" en el menú de la izquierda si quieres ver el listado de herramientas IA para la generación de imágenes
* Selecciona "Texto" en el menú de la izquierda si quieres ver el listado de herramientas IA basadas en grandes modelos de lenguaje que te servirán para procesar y/o generar texto.
* Selecciona "Audio" en el menú de la izquierda si quieres ver el listado de herramientas IA para el procesamiento de audio.
* Selecciona "Otros" en el menú de la izquierda si quieres ver otras herramientas que pueden ser de utilidad para el proceso de innovación.
* Recuerda que estas experimentando y lo importante, más que el resultado, es reconocer las ventajas de la IA.

	\n \n \n NOTA: Esta herramienta es un demo experimental y está sujeta a la demanda de uso. 

	"""




if selected == "Texto":
		st.title(f"Herramientas IA para el procesamiento de texto")
		st.write("Algunas herramientas:")




		if st.button("Generate PDF"):

			WKHTMLTOPDF_CMD = subprocess.Popen(['which', os.environ.get('WKHTMLTOPDF_PATH', '/app/bin/wkhtmltopdf')],
			stdout=subprocess.PIPE).communicate()[0].strip()
			config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_CMD)
			output_pdf = 'pdf_generado.pdf'


			# generate the PDF file as a bytes object
			pdf_bytes = pdfkit.from_string(output_text, output_pdf, configuration=config, css='style.css')
			# download the PDF file
			
			if pdf_bytes  is not None:
				st.success("PDF file Generated. Click on 'Download PDF' to save.")
				b64 = base64.b64encode(pdf_bytes ).decode()
				href = f'<a href="data:application/pdf;base64,{b64}" download="{"archivo.pdf"}">Download PDF file</a>'
				st.markdown(href, unsafe_allow_html=True)
				# remove the success message and download link
				st.empty()
			else:
				st.warning("PDF file generation failed. Please try again.")






		if st.button('Say hello'):
			st.write('Why hello there')
			
			WKHTMLTOPDF_CMD = subprocess.Popen(['which', os.environ.get('WKHTMLTOPDF_PATH', '/app/bin/wkhtmltopdf')],
			stdout=subprocess.PIPE).communicate()[0].strip()
			config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_CMD)
			output_pdf = 'pdf_generado.pdf'
			pdfoutput=pdfkit.from_string(output_text, output_pdf, configuration=config, css='style.css')
			st.success("Generación completada")
			#st.download_button('Descargar archivo pdf .pdf con tu ID', pdfoutput, file_name='pdfoutput.pdf')


			#st.write(result["text"])
		else:
			st.write('Goodbye')





if selected == "Audio":


		st.title(f"Herramientas IA para el procesamiento de audio")
		st.write("Algunas herramientas:") 
		"""
		* Herramientas para transcribir textos:
			* https://podcastle.ai/
			* https://www.notta.ai/
			* Herramienta para extraer audio de un video: https://audio-extractor.net/es/
		"""

if selected == "Otras":

		st.title(f"Otras herramientas que pueden ser útiles")
		st.write("Algunas herramientas:")
		"""
		* Herramientas para el procesamiento de audio:
			* Herramienta para hacer videos: Microsoft Climchamp (para editar videos, recortar, etc): https://clipchamp.com/ 

		"""








if selected == "Créditos":
	st.title(f"Seleccionaste la opción {selected}")
	st.write(' ')
	st.write(' ')
	st.subheader("Qüid Lab")
	body = '<a href="https://www.quidlab.co">https://www.quidlab.co</a>'
	linkedin = 'Linkedin: <a href="https://www.linkedin.com/in/jorgecif/">https://www.linkedin.com/in/jorgecif/</a>' 
	twitter = 'Twitter (X): <a href="https://twitter.com/jorgecif/">https://twitter.com/jorgecif/</a>' 
	st.markdown(body, unsafe_allow_html=True)
	st.write('Creado por: *Jorge O. Cifuentes* :fleur_de_lis:')
	st.markdown(linkedin, unsafe_allow_html=True)
	st.markdown(twitter, unsafe_allow_html=True)

	st.write('Email: *jorge@quidlab.co* ')
	st.write("Quid Lab AI tools")
	st.write("Version 1.0")
	st.text("")







