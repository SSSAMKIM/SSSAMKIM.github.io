import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from itertools import product
import numpy as np
from scipy.signal import butter, lfilter, hilbert

def plot_history(hist:dict, xlabel:str, ylabel:str):
    labels = list(hist.keys())
    plt.plot(range(len(hist[labels[0]])), hist[labels[0]], 'b', label = labels[0])
    plt.plot(range(len(hist[labels[1]])), hist[labels[1]], 'r', label = labels[1])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(loc='upper right')
    plt.tight_layout()
    
def fft_th(data, sampling_frequency, label, true = 1, mode = 1):
    y =data-np.mean(data)
    yf = np.fft.fft(y)/len(y)
    xf = np.fft.fftfreq(len(y))
    xf=xf*sampling_frequency
    xf_=xf[:np.argmax(xf)]
    yf_ = np.abs(yf[:np.argmax(xf)])
    
    if mode==1:
        if true:
            plt.plot(xf_, np.abs(yf_), 'r', label = label)
        else:
            plt.plot(xf_, np.abs(yf_), 'b', label = label)
    
#     if mode==1:
#         plt.plot(xf_, np.abs(yf_), label = label)
#         plt.legend(loc = 'upper right')
#         plt.xlim([0,100])
    return xf_, yf_

'''dataset 내에 class별 평균 kde'''
def gaussian_kde_RK4(dataset, n_data:int, n_class:int, aug:bool, n_aug:int=3, X_interest:np=np.arange(-2,2,0.1)):
    labels = ['Misalignment', 'Oil Whirl', 'Rubbing', 'Unbalance']
    n_each = int(n_data/n_class)
    kde_list, kde_each = [], []
    sig_list, sig_each = [], []
    cnt = 0
    for idx, (X,y) in enumerate(dataset):
        if aug:
            signal = X.detach().cpu().numpy().reshape(1,-1)
            estimator = gaussian_kde(signal)
            density = estimator(X_interest)
            kde_each.append([density])
            sig_each.append([signal])

            if int((idx + 1) % n_each) == 0 and idx != 0:
                print(f'{labels[cnt]}: done')
                kde_list.append(kde_each)
                sig_list.append(sig_each)
                kde_each = []
                cnt += 1
            
        else:
            if idx % n_aug == 0:
                signal = X.detach().cpu().numpy().reshape(1,-1)
                estimator = gaussian_kde(signal)
                density = estimator(X_interest)
                kde_each.append([density])
                sig_each.append([signal])

                if int((idx + n_aug) % n_each) == 0 and idx != 0:
                    print(f'{labels[cnt]}: done')
                    kde_list.append(kde_each)
                    sig_list.append(sig_each)
                    kde_each = []
                    cnt += 1
    
    n_kde_each = n_each if aug else int(n_each/n_aug)
    
    kde_arr = np.array(kde_list).reshape(n_class, n_kde_each, len(X_interest))
    
    return sig_list, kde_arr

def KLD(p,q,eps):
    return sum((p+eps)*np.log((p+eps)/(q+eps)))

def JSD(p,q,eps):
    M = 0.5*(p+q)
    return np.sum(0.5*KLD(p,M,eps) + 0.5*KLD(q,M,eps))

def butter_bandpass(low_cut, high_cut, sf, order=5):
    nyq = 0.5 * fs
    low = low_cut / nyq
    high = high_cut / nyq
    b, a = butter(order, [low, high], btype = 'band')
    return b,a

def butter_bandpass_filter(data, low_cut, high_cut, sf, order=5):
    b, a = butter_bandpass(low_cut, high_cut, sf, order)
    y = lfilter(b, a, data)
    return y

def hilbert_transform(signal):
    analytic_signal = hilbert(signal)
    amplitude_envelope = np.abs(analytic_signal)
    return amplitude_envelope

def conv1d_dim(input_dim, params:dict):
    x = []
    for idx in range(len(params['kernel'])):
        k, p, d, s = params['kernel'], params['padding'], params['dilation'], params['stride']
        if input_dim <= k[idx]: raise Exception('Input dimension is lower than the kernel size')
        x.append(int((input_dim + 2*p[idx] - d[idx] * (k[idx]-1) - 1)/s[idx]) + 1)
        print(f'Conv layer {idx+1} output dim: {x[idx]}')
        input_dim = x[idx]
    return x

def convT1d_dim(input_dim, params:dict):
    x = []
    for idx in range(len(params['kernel'])):
        k, p, d, s = params['kernel'], params['padding'], params['dilation'], params['stride']
        x.append((input_dim-1)*s[idx] - 2*p[idx] + d[idx] * (k[idx]-1) + 1)
        print(f'ConvTranspose layer {idx+1} output dim: {x[idx]}')
        input_dim = x[idx]
        
    return x
