try:
    import pandas as pd
    import matplotlib.pyplot as plt
    import mplcursors as mpc
    
    # URL of the data source
    url = "https://comune.venezia.it/sites/default/files/publicCPSM2/stazioni/temporeale/Piattaforma.html"
    url2 = "https://comune.venezia.it/sites/default/files/publicCPSM2/stazioni/temporeale/Punta_Salute.html"
    url3 = "https://comune.venezia.it/sites/default/files/publicCPSM2/stazioni/temporeale/Burano.html"

    # Read the data from the URL
    data = pd.read_html(url)[0]
    data2 = pd.read_html(url2)[0]
    data3 = pd.read_html(url3)[0]

    # Extract the first and second columns for x and y axes
    x = data.iloc[:, 0]
    y = data.iloc[:, 1]
    z = data2.iloc[:, 1]
    w = data3.iloc[:, 1]
    
    # Plot the data on a line chart
    plt.figure(figsize=(12, 9))
    plt.plot(x, y, marker='.', linestyle='-', color='b', label="Piattaforma CN")
    plt.plot(x, z, marker='.', linestyle='-', color='c', label ="Punta salute")
    plt.plot(x, w, marker='.', linestyle='-', color='r', label="Burano")
    plt.axhline(y=0, color='black', linewidth=0.5)
    plt.legend (ncol=3, mode="expand", loc="lower center")
    #plt.text (0,0, data.iloc[-1:, 0], ha="center", va="center")
    d=data.iloc[-1:,0].to_string(header=False, index=False)[-17:]
    
    plt.xlabel('Data')
    plt.ylabel('Altezza sul livello del mare')
    
    plt.title('Maree Laguna di Venezia - Ultimo dato:'+d)
    plt.grid(False)
    plt.tight_layout()

    plt.xticks(ticks=x[::50], rotation=0)
    
    mpc.cursor(hover=True)
    plt.show()   

except ImportError as e:
    print(f"ImportError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")