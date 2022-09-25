
def print_hash_line(line=None, symbol='#', newline=False):
    for i in range(24):
        print(symbol, end=" ")
        if i == 23: print("")
    if line==None:
        if newline:
            print("")
        return  
    print(f"{symbol} ",line)
    for i in range(24):
        print(symbol, end=" ")
        if i == 23: print("")
    if newline:
        print("")

def plot_particles(data_path="data.csv"):
    
    import plotly.express as px
    import pandas as pd 
    
    df = pd.read_csv(data_path,index_col=0)

    fig = px.scatter_3d(df, x='x', y='y', z='z',animation_frame=df.index,
                        range_x=[0,1e-6],range_y=[0,1e-6],range_z=[0,1e-6]
                )
    fig.update_traces(marker={"size":2})
    fig.show() 

