from scipy.io import wavfile as wav
import numpy as np
#import matplotlib.pyplot as plt
from multiprocessing import Process
import subprocess, time
import booboochoochoo as bo

FileName = "NYC.wav"

# import wave
# infiles = ["100hz.wav", "200hz.wav", "500hz.wav", "1000hz.wav", "2000hz.wav", "5000hz.wav", "15000hz.wav", "20000hz.wav"]
# outfile = "sounds.wav"
#
# data= []
# for infile in infiles:
#     w = wave.open(infile, 'rb')
#     data.append( [w.getparams(), w.readframes(w.getnframes())] )
#     w.close()
#
# output = wave.open(outfile, 'wb')
# output.setparams(data[0][0])
# output.writeframes(data[0][1])
# output.writeframes(data[1][1])
# output.writeframes(data[2][1])
# output.writeframes(data[3][1])
# output.writeframes(data[4][1])
# output.writeframes(data[5][1])
# output.writeframes(data[6][1])
# output.writeframes(data[7][1])
# output.close()
def play_audio(file = None):
    try:
        return_code = subprocess.call(["aplay", file])
    except Exception as e:
        print(e)



def read_wave_file():
    # fileNamePath = input("Drag your audio file here: ")
    # fileName = fileNamePath.split("/")[-1]
    # bit_rate, wave_data = wav.read(fileName[:-1])
    bit_rate, wave_data = wav.read(FileName)
    if len(wave_data.shape) > 1:
        audio_channel = wave_data.shape[1]
    else:
        audio_channel = 1
    audio_samples_per_channel = wave_data.shape[0]
    sound_duration = audio_samples_per_channel / bit_rate
    print("audio bit rate is: {}\n"
          "audio bit type is: {}\n"
          "audio channel is: {}\n"
          "audio samples: {}\n"
          "audio duration is {}s\n"
          .format(bit_rate,wave_data.dtype.name, audio_channel,audio_samples_per_channel,sound_duration))
    normalization_factor = int(wave_data.dtype.name[-2:])-1
    # print(normalization_factor)
    if len(wave_data.shape) > 1:
        channel_1 = wave_data[:,0] / (2.** normalization_factor)
    else:
        channel_1 = wave_data[:] / (2. ** normalization_factor)
    return channel_1, bit_rate, audio_samples_per_channel, sound_duration


def slice_wave_data(raw_data = None, slice_duration = 1.0):

    # print("total sample", raw_data[2])
    # print ("slice_duration_sample",raw_data[1] * slice_duration)
    slice_divider = list(np.arange(int(raw_data[1] * slice_duration), raw_data[2], int(raw_data[1] * slice_duration)))
    # print("debug divider {}, type{}".format(slice_divider, type(slice_divider)))
    slice_list_tu = []
    slice_list = np.split(raw_data[0],slice_divider)
    # for i in np.split(raw_data[0],slice_divider):
    #     print(i.size)
    for i in slice_list:
        slice_list_tu.append([i,raw_data[1], raw_data [2], raw_data[3]])
    return slice_list_tu


def plot_wave_in_time_domain(raw_data = None):
    x_axis = np.arange(0, raw_data[0].size, 1) / raw_data[1] * 1000
    fig, time_domain_plot = plt.subplots()
    time_domain_plot.plot(x_axis, raw_data[0], 'r-')
    time_domain_plot.set_title("time")
    time_domain_plot.set_xlabel('time in ms')
    time_domain_plot.set_ylabel("Power", color='r')
    plt.show()


def find_next_pwr_2 (x = None):
    x = int(x)
    return 1 if x == 0 else (2**(x-1).bit_length())


def fft_data(raw_data = None,):
    fft_sampling_space = find_next_pwr_2(raw_data.size)
    sampling_point_fft = np.fft.fft(raw_data, fft_sampling_space)
    sampling_point_fft = sampling_point_fft[0: int(sampling_point_fft.size / 2)]
    # print(sampling_point_fft.size)
    sample_amp = (np.absolute(sampling_point_fft)/sampling_point_fft.size) ** 2
    # print("amp size {}".format(sample_amp.size))
    return sample_amp


def plot_data_in_frq_domain(fft_data=None, sample_space = 1000, band_with_error = 0.2,
                            band = [100,200,500,1000,2000,5000,10000,15000], sacle = 1 ):
    # print("Y_axis: fft data: {}".format(fft_data))
    # print("sample space",sample_space)
    # print("fft_data.size",fft_data.size)
    x_axis = np.arange(0, fft_data.size, 1) * sample_space / fft_data.size
    # print("x_axis", x_axis)
    # fig, frq_domain_plot = plt.subplots()
    # frq_domain_plot.plot(x_axis, fft_data, 'r-')
    # plt.xscale('log')
    # frq_domain_plot.set_title("frequency")
    # frq_domain_plot.set_xlabel('frequency in Hz')
    # frq_domain_plot.set_ylabel("Power", color='r')
    # plt.show()

    max_amp = max(list(ffted_data))
    # print("max amp", max_amp)
    combine_data = np.dstack((x_axis,fft_data))
    # print("type",type(ffted_data))

    # print(combine_data)
    # print("first data {} type {}".format(combine_data[0][0][1], type(combine_data[0][0])))
    filted_data_list = []
    for i in band:
        filted_data = [j for j in combine_data[0] if i- i*band_with_error < j[0] < i+i*band_with_error]
        # print("filter frq",filted_data)
        if len(filted_data) == 0:
            print("No data")
        filted_data_list.append(filted_data)
    # print(filted_data_list)
        # fig, frq_domain_plot_div = plt.subplots(8,1)
        # frq_domain_plot_div.plot([m[0] for m in filted_data], [n[1] for n in filted_data], 'r-')
        # frq_domain_plot_div.set_title("Bnad with {}".format(i))
        # frq_domain_plot_div.set_xlabel('frequency')
        # frq_domain_plot_div.set_ylabel("Power", color='r')
        # index += 1
        # print(index)
    # print("slice frq data ",filted_data_list[0][0])
    # print("slice frq data ", filted_data_list[0])
    result = []
    for i in filted_data_list:
        #print("debug list",[j[1] for j in i])
        amp = max([j[1] for j in i])/sacle * 1000
        result.append(amp)
    print("result",result)
    return result, max_amp



if __name__ == "__main__":
    data_list = read_wave_file()
    # plot_wave_in_time_domain(data_list)
    # ffted_data = fft_data(data_list[0])
    # data, maxamp = plot_data_in_frq_domain(fft_data=ffted_data, sample_space=ffted_data.size, band_with_error=0.2,
    #                        band=[100, 200, 500, 1000, 2000, 5000, 10000, 15000],sacle = 1 )

    # print ("debug maxamp",maxamp)
    slice_list = slice_wave_data(raw_data = data_list, slice_duration = 1)

    # p = Process(target=play_audio, args=(FileName,))
    # p.start()
    bo.initi()
    print("Start here\n\n")
    for i in slice_list:
        # print(i)
        # plot_wave_in_time_domain(i)
        start_time = time.time()
        ffted_data = fft_data(i[0])
        a = plot_data_in_frq_domain(fft_data = ffted_data, sample_space=ffted_data.size, band_with_error = 0.2,
                            band = [100,200,500,1000,2000,5000,10000,15000],sacle = 0.0006253)[0]
        bo.extract(a)
        print("debug",a)
        last_time = time.time()-start_time
        print ("time last",time.time()-start_time)
        #time.sleep(10-last_time)

    #p.join()
