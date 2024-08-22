import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
import numpy as np

#================================================
# PLOTTING USING MATPLOTLIB.PYPLOT

def plt_plot(x_train, y_train, x_test, y_test, x, y_predictions, samples_to_show, show_suptitle, bnn_type):
    fig, axs = plt.subplots(1, 2, constrained_layout=True, figsize=(8, 4))

    #------------------------------------
    # Plotting the training data:
    axs[0].scatter(x_train, y_train, s=2, label='Training Data')

    # Obtaining and plotting multiple predictions:
    for i in range(y_predictions.shape[0]):
        # Plotting the prediction:
        axs[0].plot(x, y_predictions[i], linewidth=2)
    
    # Final formatting for the plot:
    axs[0].set_title('For Training Data')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('y')
        
    #------------------------------------
    # Plotting the test data:
    axs[1].scatter(x_test, y_test, s=2, label='Test Data') 
    
    # Obtaining and plotting multiple predictions:
    for i in range(y_predictions.shape[0]):
        # Plotting the prediction:
        axs[1].plot(x, y_predictions[i], linewidth=2)
    
    # Final formatting for the plot:
    axs[1].set_title('For Test Data')
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('y')

    #------------------------------------
    if show_suptitle:
        plt.suptitle(f'Multiple Predictions of {bnn_type}')
    plt.show()

#================================================
# PLOTTING USING SEABORN

def sb_plot(x_train, y_train, x_test, y_test, x, y_predictions, samples_to_show, show_suptitle, bnn_type):
    fig, axs = plt.subplots(1, 2, constrained_layout=True, figsize=(8, 4))

    #------------------------------------
    X = np.transpose(np.array([x.flatten()]*y_predictions.shape[0])).flatten()
    Y = np.transpose(y_predictions).flatten()
    '''
    NOTE: Shape before the final flattening:
    Before the final flattening, the shape of each X and Y is in the form:
    (number of predictions, number of unique x values)
    '''
    df = pd.DataFrame({'X':X, 'Y':Y})
    
    #------------------------------------
    # Plotting the training data:
    sb.scatterplot(x=x_train.flatten(), y=y_train.flatten(), size=2, legend=False, ax=axs[0])
    sb.lineplot(data=df, x='X', y='Y', errorbar=lambda Y: (Y.min(), Y.max()), ax=axs[0], label='Range')
    sb.lineplot(data=df, x='X', y='Y', errorbar='ci', ax=axs[0], label='95% CI')
    
    # Final formatting for the plot:
    axs[0].set_title('For Training Data')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('y')
        
    #------------------------------------
    # Plotting the test data:
    sb.scatterplot(x=x_test.flatten(), y=y_test.flatten(), size=2, legend=False, ax=axs[1])
    sb.lineplot(data=df, x='X', y='Y', errorbar=lambda Y: (Y.min(), Y.max()), ax=axs[1], label='Range')
    sb.lineplot(data=df, x='X', y='Y', errorbar='ci', ax=axs[1], label='95% CI')
    
    # Final formatting for the plot:
    axs[1].set_title('For Test Data')
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('y')

    #------------------------------------
    if show_suptitle:
        plt.suptitle(f'Multiple Predictions of {bnn_type}')
    plt.show()

#================================================
# FUNCTION TO CHOOSE THE GIVEN PLOT VERSION(S)

def plot_function(x_train, y_train, x_test, y_test, x, y_predictions, samples_to_show, show_suptitle, version, bnn_type):
    plot_function = {1:plt_plot, 2:sb_plot, 'all':[plt_plot, sb_plot]}[version]
    try:
        plot_function(x_train, y_train, x_test, y_test, x, y_predictions, samples_to_show, show_suptitle, bnn_type)
    except:
        for f in plot_function:
            f(x_train, y_train, x_test, y_test, x, y_predictions, samples_to_show, show_suptitle, bnn_type)