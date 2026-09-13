
import matplotlib.pyplot as plt

def scatter_plot(x_data, y_data, graph_title, x_label, y_label, labels=None, colors="salmon", file_name_to_save=None):
    '''Plot the data scatterly in the graph based on the x_data and the y_data 

    Args: 
        x_data : X-axis data to plot in the graph
        y_data : Y-axis data to plot in the graph
        graph_title : Title to put on the graph
        x_label : label for the x-axis data 
        y_label : label for the y-axis data 
        labels ( List[str] ) : if None then no labels are applied to the graph and if label are provided than the label's are adjusted in the graph (make sure to pass the label in the list of String).
        colors (List[str]) : accepts the list of the valid color's.
        file_name_to_save : if provided the graph will be saved to the given path.

    Returns:
        matplotlib graph 
    '''

    plt.figure(figsize=(10, 6))

    # scatter plot 
    plt.scatter(
        x=x_data,
        y=y_data,
        c=colors
    )

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(graph_title)

    if labels:
        plt.legend(labels)

    if file_name_to_save:
        plt.savefig(file_name_to_save)
    
    return plt.show()


def bar_plot(x_data, graph_title, x_label, y_label, figsize=None, labels=None, colors=["salmon"], file_name_to_save=None):
    '''Bar graph plot for the given x_data 
    
    Args: 
        x_data : X-axis data to plot in the graph
        graph_title : Title to put on the graph
        x_label : label for the x-axis data 
        y_label : label for the y-axis data 
        figsize (tuple(int, int)) : figure size of the graph  
        labels ( List[str] ) : if None then no labels are applied to the graph and if label are provided than the label's are adjusted in the graph (make sure to pass the label in the list of String).
        colors (List[str]) : accepts the list of the valid color's.
        file_name_to_save : if provided the graph will be saved to the given path.

    Returns:
        matplotlib graph 
    
    '''

    if figsize:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig, ax = plt.subplots()

    ax = x_data.plot(kind='bar', color=colors, ax=ax);

    
    ax.set(xlabel=x_label, 
           ylabel=y_label,
           title=graph_title)
    
    
    plt.xticks(rotation=0)

    if labels:
        ax.legend(handles=labels)

    if file_name_to_save:
        plt.savefig(file_name_to_save)

    return plt.show()