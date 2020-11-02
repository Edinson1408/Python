#Grafica simple en python
#utilizamoe el Bokeh que nos permite contruir graficos complejos de manera rapida y con comando simples
#permite exportar a varios doemacos como html, notebooks, imageners.etc
#bokeh se puede utilizar en el sevidor con lask y Django

# figure para la figura que realizaremos
# output_file para el archivo hmtl que generaremos
# show es un servidor que nos ayuda a mostrar el archivo html
#plotting graficado
from bokeh.plotting import figure,output_file,show

if __name__ =='__main__':
    output_file('graficado_simple.html')
    fig=figure()

    total_valores=int(input('Cuantos valores quiere graficar : '))
    x_val=list(range(total_valores))
    y_val=[]

    for x in x_val:
        val=int(input(f'Iserte el valor y para {x} : '))
        y_val.append(val)
    
    fig.line(x_val,y_val,line_width=2)
    show(fig)

    #para mostar esto ,en consola tenemos que hcer los siguientes pasos
