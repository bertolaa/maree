try:
    import pandas as pd
    import matplotlib.pyplot as plt

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
    plt.figure(figsize=(15, 12))
    plt.plot(x, y, marker='.', linestyle='-', color='b')
    plt.plot(x, z, marker='.', linestyle='-', color='c')
    plt.plot(x, w, marker='.', linestyle='-', color='r')
        
    plt.xlabel('Data')
    plt.ylabel('Altezza sul livello del mare')
    
    plt.title('Maree Laguna di Venezia')
    plt.grid(False)
    plt.tight_layout()
    #plt.xticks (rotation=45)
    plt.xticks(ticks=x[::50], rotation=20)
    plt.text(0.5,0.5, "Piattaforma CNR",fontsize=12, color='b')
    plt.text(0.5,0.6, "Punta salute",fontsize=12, color='c')
    plt.text(0.5,0.7, "Burano", fontsize=12, color='r')
    

    # Show the plot
    plt.show()

except ImportError as e:
    print(f"ImportError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
