# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "ipython>=9.11.0",
#     "librosa>=0.11.0",
#     "marimo>=0.20.2",
#     "matplotlib>=3.10.8",
#     "numpy>=2.4.3",
#     "pyzmq>=27.1.0",
#     "scipy>=1.17.1",
# ]
# ///

import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **Assignment 1: Sound Processing Fundamentals**
    ### Due: Thursday, February 5th, midnight EST
    ### Quiz date: Tuesday, February 10th in-class

    CS-GY 6933: Machine Listening Spring 2026

    Below you will find a mix of coding questions and writing questions to familiarize you with the fundamentals of signal processing in Python.

    The assignment will have two parts:

    1. Part 1: **Tutorial**: code snippets and tools to help you with the core problem in Part 2. This portion is not worth any points and typically will not have anything to "fill-in". I recommend you walk through the code and run it to understand the pieces before moving to Parts 2-3.

    2. Parts 2-3: **Problem solving**: core part of the assignment, with two-part multi-step problem solving tasks. This will be worth 5 points total. The in-class quiz about the assignment will also be worth 5 points.

    When you complete the assignment, please evaluate the notebook so that all results are shown/printed before submitting via Brightspace.

    🚨 Please refrain from using ChatGPT etc. to fully write the code for this assignment. You will need to understand the content to succeed in the in-class quiz.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **Part 1:** Tutorial - Basics of working with digital signals in Python
    Note: this section is not worth any points. It is here to help you/give you the basic tools to help with Part 2. **You will use the `get_sinewave`** method in the following sections so be sure to run each cell here.
    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    import IPython # useful for playing audio in the notebook
    import librosa
    from scipy import signal

    return IPython, librosa, np, plt, signal


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Basics
    Let's start by getting familiar with the basics of working with audio signals in Python.

    First, recall the equation for the simplest periodic wave, a **sinusoid**:

    $x(t) = A * sin(2\pi ft + \theta)$

    where $A$ is amplitude, $f$ is frequency, $t$ is time, and $\theta$ is phase.

    **Let's check out a function that implements this question, generating a sine wave:**
    """)
    return


@app.cell
def _(np):
    def get_sinewave(amplitude, frequency, duration, sr, phase=0):
        """
        Generate a sine wave signal.

        Parameters:
        ----------
        amplitude : float
            The peak amplitude of the sine wave.
        frequency : float
            The frequency of the sine wave in Hertz (Hz).
        duration : float
            The duration of the sine wave in seconds.
        sr : int
            The sampling rate, in samples per second (Hz).
        phase : float, optional
            The initial phase of the sine wave in radians. Default is 0.

        Returns:
        -------
        numpy.ndarray
            A 1D array containing the generated sine wave samples.
        """
        _num_samples = int(sr * duration)
        time_samples = np.linspace(0, duration, _num_samples)
        return amplitude * np.sin(2 * np.pi * frequency * time_samples + phase)

    return (get_sinewave,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We will be doing a lot of **plotting** of audio signals in this class. We will use a combination of `matplotlib` and occasionally `librosa`'s plotting features for this. Let's create some waveforms and plot them to better-understand how choice of amplitude, frequency, phase, and sample rate work. Note that the dummy parameters chosen for the sample waveforms here are not what you'll typically use for real audio and more for illustrative purposes (e.g. a sample rate of 100 is suuuuper low- normally you'll see something like 16kHz or 48kHz.
    """)
    return


@app.cell
def _(get_sinewave, plt):
    # Use the function to generate two sinewaves
    _duration = 1
    sr = 100
    wav1 = get_sinewave(amplitude=1, frequency=100, duration=_duration, sr=sr, phase=0)
    wav2 = get_sinewave(amplitude=0.5, frequency=400, duration=_duration, sr=sr, phase=0)
    plt.plot(wav1, marker='.', color='tab:blue')
    # Plot them overlayed
    plt.plot(wav2, marker='.', color='orange')
    plt.ylabel('Amplitude')
    plt.xlabel('Time (samples)')
    plt.title('Simple Sinewaves')
    plt.gcf()
    return


@app.cell
def _(get_sinewave, np, plt):
    _duration = 1
    sr_1 = 100
    wav1_1 = get_sinewave(amplitude=1, frequency=100, duration=_duration, sr=sr_1, phase=0)
    wav2_1 = get_sinewave(amplitude=0.5, frequency=400, duration=_duration, sr=sr_1, phase=0)
    _num_samples = int(sr_1 * _duration)
    _time_in_seconds = np.linspace(0, _duration, _num_samples, endpoint=False)
    plt.plot(_time_in_seconds, wav1_1, marker='.', color='tab:blue')
    plt.plot(_time_in_seconds, wav2_1, marker='.', color='orange')
    plt.ylabel('Amplitude')
    plt.xlabel('Time (seconds)')
    plt.title('Simple Sinewaves')
    plt.gcf()
    return


@app.cell
def _(get_sinewave, np, plt):
    _duration = 1
    sr_2 = 100
    wav1_2 = get_sinewave(amplitude=1, frequency=100, duration=_duration, sr=sr_2, phase=0)
    wav2_2 = get_sinewave(amplitude=0.5, frequency=400, duration=_duration, sr=sr_2, phase=0)
    sum_wave = wav1_2 + wav2_2
    _num_samples = int(sr_2 * _duration)
    _time_in_seconds = np.linspace(0, _duration, _num_samples, endpoint=False)
    plt.plot(_time_in_seconds, sum_wave, marker='.', color='tab:blue')
    plt.ylabel('Amplitude')
    plt.xlabel('Time (seconds)')
    plt.title('Simple Sinewaves')
    plt.gcf()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Cool! Compare the plot above with the individual waveforms and check out the effect.
    """)
    return


@app.cell
def _(get_sinewave, np, plt):
    _duration = 1
    sr_3 = 100
    wav1_3 = get_sinewave(amplitude=1, frequency=200, duration=_duration, sr=sr_3, phase=0)
    wav2_3 = get_sinewave(amplitude=1, frequency=200, duration=_duration, sr=sr_3, phase=np.pi)
    _num_samples = int(sr_3 * _duration)
    _time_in_seconds = np.linspace(0, _duration, _num_samples, endpoint=False)
    plt.plot(_time_in_seconds, wav1_3, marker='.', color='tab:blue')
    plt.plot(_time_in_seconds, wav2_3, marker='.', color='orange')
    plt.ylabel('Amplitude')
    plt.xlabel('Time (seconds)')
    plt.title('Simple sinewaves')
    plt.gcf()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Listening to audio in Python
    Fun plots, but of course we also want to ***hear*** our audio! We'll use the `IPython` package for this typically.

    Let's generate waveforms with more reasonable parameters and listen to them.
    """)
    return


@app.cell
def _(get_sinewave, plt):
    _duration = 3
    sr_4 = 16000
    wav1_4 = get_sinewave(amplitude=1, frequency=440, duration=_duration, sr=sr_4, phase=0)
    wav2_4 = get_sinewave(amplitude=1, frequency=2000, duration=_duration, sr=sr_4, phase=0)
    _num_samples = int(sr_4 * _duration)
    plt.plot(wav1_4[:200], marker='.', color='tab:blue')
    plt.plot(wav2_4[:200], marker='.', color='orange')
    plt.ylabel('Amplitude')
    plt.xlabel('Time (samples)')
    plt.title('Simple sinewaves')
    plt.gcf()
    return wav1_4, wav2_4


@app.cell
def _(IPython, wav1_4):
    # Listen to waveform 1
    IPython.display.Audio(wav1_4, rate=16000)
    return


@app.cell
def _(IPython, wav2_4):
    # Listen to waveform 2
    # Yay! We can hear a difference in frequency :)
    IPython.display.Audio(wav2_4, rate=16000)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's also make sure you know how to **load a real-world audio clip** in Python.

    **[Librosa](https://librosa.org/doc/latest/index.html)** is an awesome library for audio processing in Python, created by Brian McFee (NYU Professor!). We will use Librosa a lot in this class.

    For now let's just load files with Librosa: https://librosa.org/doc/0.10.2/generated/librosa.load.html#librosa-load.
    """)
    return


@app.cell
def _(librosa, np, plt):
    filename = librosa.ex('trumpet')
    y, sr_5 = librosa.load(filename, sr=None)
    print(f'Number of samples: {len(y)}')
    print(f'Sampling rate: {sr_5}')
    print(f'Duration: {len(y) / sr_5} seconds')
    _time_in_seconds = np.linspace(0, len(y) / sr_5, len(y))
    plt.plot(_time_in_seconds, y)
    plt.ylabel('Amplitude')
    plt.xlabel('Time (seconds)')
    plt.title('Audio Signal')
    plt.gcf()
    return sr_5, y


@app.cell
def _(IPython, y):
    # And lastly let's listen to it! Listen and follow the plot along.
    IPython.display.Audio(y, rate=22050)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **Part 2:** DSP Problem Solving with the **DFT** *[3 pts]*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### DFT Implementation *[0.5 pt]*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Implement the **DFT** using the equation given in class:

    $ X(k) = \langle x(n), s_k(n)\rangle$

    $s_k(n) = e^{\frac{-j2πnk}{N}}$

    where:

    - $x$: input signal
    - $N$: number of time/frequency samples in $x$
    - $n$: current integer sample ($x$ has samples $n=0$ to $N-1$)
    - $j$: imaginary number 😺
    - $k$: current frequency where $k \in [0, N-1]$
    - $X$: spectrum of X (e.g. output of DFT)

    This will be evaluated via test cases looking for the correct output shape (within some small tolerance) as well as how it functions within your spectrum function, which we will see via plots.
    """)
    return


@app.cell
def _(np):
    # TODO: Implement the DFT function from scratch. [0.5 pt]
    def DFT(x):
        """
        Compute the Discrete Fourier Transform (DFT) of a 1-D real or complex signal.

        This function should implement the DFT *from scratch* using the
        definition discussed in class and above.

        Parameters
        ----------
        x : array_like, shape (N,)
            Input time-domain signal (real or complex).

        Returns
        -------
        X : ndarray, shape (N,)
            Complex DFT of the input signal, containing both magnitude
            and phase information.

        Notes
        -----
        - This implementation is for educational purposes and should NOT
          use `np.fft.fft` or any FFT library.

        """
        x = np.asarray(x, dtype=complex)
        N = len(x)

        # allocate output
        X = np.zeros(N, dtype=complex)
        n = np.arange(N)
        k = n.reshape(-1,1)

        # complex sinusoid (basis vector for freq m)
        Wm = np.exp(-1j * 2 * np.pi * k * n / N)

        # dot product between signal & basis vector
        X = np.dot(Wm, x)

        return X

    return (DFT,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Spectrum Implementation *[0.5 pt]*
    Next, let's take this a step further by computing the **spectrum** of a signal, using our DFT code above. This will be evaluating via test cases looking for the correct output shape (within some small tolerance) as well as through your spectrum plots below.

    **Hint:** recall that frequency resolution is defined by $ sr / N$ and temporal resolution as $1 / sr$, where $sr$ is the sampling rate.
    """)
    return


@app.cell
def _(DFT, np):
    def compute_basic_spectrum(x, sr):
        """
        Compute a magnitude spectrum using the DFT.

        # Ensure that both the frequency bins and amplitude bins:
        # - do not contain complex values
        # - do not contain the symmetric component

        Remember to normalize your final magnitude values.

        Parameters
        ----------
        x : np.ndarray
            1D time-domain signal.
        sr : int
            Sampling rate in Hz.

        Returns
        -------
        freqs_hz : np.ndarray
            Frequency axis (Hz) for the DFT bins.
        mags : np.ndarray
            Magnitude spectrum, **normalized**.

        """
        N = len(x)
        X = DFT(x)
        _mags = np.abs(X)
        _mags = _mags / N
        freqs_hz = np.arange(N) * sr / N
        half = N // 2 + 1
        freqs_hz = freqs_hz[:half]
        _mags = _mags[:half]
        if N % 2 == 0:
            _mags[1:-1] = _mags[1:-1] * 2
        else:
            _mags[1:] = _mags[1:] * 2
        return (freqs_hz, _mags)

    return (compute_basic_spectrum,)


@app.cell
def _(plt):
    # BUILT-IN: Use this built-in code for plotting the spectrum to check your results
    def plot_spectrum(freqs_hz, mags, title=None):
        """
        Plot the magnitude spectrum of a signal.

        Parameters
        ----------
        freqs : array_like
            Frequency values in Hz.
        mags : array_like
            Magnitude of the DFT at each frequency.
        title : str, optional
            Plot title.
        """
        plt.figure(figsize=(6, 4))
        plt.stem(freqs_hz, mags, 'b', markerfmt=' ', basefmt='-b')
        plt.xlabel('Freq (Hz)')
        plt.ylabel('DFT  Magnitude |X(freq)|')
        plt.title(title)
        return plt.gcf()

    return (plot_spectrum,)


@app.cell
def _(mo):
    mix = mo.ui.slider(0,1,0.1)
    mix
    return (mix,)


@app.cell
def _(compute_basic_spectrum, get_sinewave, mix, plot_spectrum, sr_5):
    x = get_sinewave(amplitude=0.5, frequency=2000, duration=0.02, sr=sr_5) + mix.value * get_sinewave(amplitude=0.5, frequency=4000, duration=0.02, sr=sr_5)
    freqs, _mags = compute_basic_spectrum(x, sr_5)
    plot_spectrum(freqs, _mags, 'Test Spectrum (2000Hz + 4000Hz)')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Problem-solving with your DFT & spectrum *[2 pts]*
    Great, we've written the tools we need to explore spectrums of different signals. However, computing the DFT and spectrum is only part of the challenge: the choice of analysis parameters is very important in analyzing discrete audio signals, and here we will dig into that.

    Below you will find a signal, `x_bad` that is a mixture of sinusoids, and an accompanying spectrum of this signal. Something is ***not quite right*** with this analysis setup. Your tasks:

    1. Identify (3) aspects of this analysis setup (may come from parameter choice and/or spectrum plot) that could be improved to more accurately represent the signal. *[1/3 pt for identifying each issue x 3]*

    2. Implement a new function, `compute_spectrum_pro`, template below. 2 out of the 3 issues should be solved inside the function, but 1 will be a choice of analysis parameter. You need to solve all 3 of these for full credit! *[1/3 pt for solving each issue x 3]*

    Note that the amplitude, frequency, duration, and phase of the signal ***cannot change***.
    """)
    return


@app.cell
def _(compute_basic_spectrum, get_sinewave, plot_spectrum):
    sr_6 = 2000
    _duration = 0.2
    _x_bad = get_sinewave(amplitude=1.0, frequency=440.5, duration=_duration, sr=sr_6, phase=0) + get_sinewave(amplitude=0.5, frequency=1320.3, duration=_duration, sr=sr_6, phase=0)
    freqs_1, _mags = compute_basic_spectrum(_x_bad, sr_6)
    plot_spectrum(freqs_1, _mags, title='Original Spectrum')
    return


@app.cell
def _(DFT, np, signal):
    def compute_spectrum_pro(x, sr, window, pad_to=None):
        """
        Compute an improved magnitude spectrum using the DFT.

        Parameters
        ----------
        x : np.ndarray
            1D time-domain signal.
        sr : int
            Sampling rate in Hz.
        window: string 
            the kind of window used
        pad_to: int
            the amount of padding desired

        Returns
        -------
        freqs_hz : np.ndarray
            Frequency axis (Hz) for the DFT bins.
        mags : np.ndarray
            Magnitude spectrum, normalized.
        """
        N = len(x)
        w = signal.get_window(window, N)
        x = x * w
        if pad_to is not None and pad_to > N:
            x = np.pad(x, (0, pad_to - N))
            N = pad_to
        X = DFT(x)
        _mags = np.abs(X) / np.sum(w)
        freqs_hz = np.arange(N) * sr / N
        half = N // 2 + 1
        freqs_hz = freqs_hz[:half]
        _mags = _mags[:half]
        if N % 2 == 0:
            _mags[1:-1] = _mags[1:-1] * 2
        else:
            _mags[1:] = _mags[1:] * 2
        return (freqs_hz, _mags)

    return (compute_spectrum_pro,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, test your new function. Remember that you are not limited to changing only parameters within the new function and **will** need to change other analysis parameters to solve every issue.
    """)
    return


@app.cell
def _(compute_spectrum_pro, get_sinewave, plot_spectrum):
    sr_7 = 4000
    _duration = 0.2
    _x_bad = get_sinewave(amplitude=1.0, frequency=440.5, duration=_duration, sr=sr_7, phase=0) + get_sinewave(amplitude=0.5, frequency=1320.3, duration=_duration, sr=sr_7, phase=0)
    freqs_2, _mags = compute_spectrum_pro(_x_bad, sr_7, 'hann', pad_to=4096)
    plot_spectrum(freqs_2, _mags, title='Improved Spectrum!')
    return (sr_7,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **Part 3**: DSP Problem Solving with the **STFT** [2 pts]
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Complete the following tasks:

    1. Write the STFT function from scratch, using the rough template below. Do not change the structure of what is returned. **You may not use Librosa, but you may use numpy.**  Instead of using your DFT function from above, it may be useful (**and faster!**) to use `np.fft.rfft` to get only the real, non-negative frequencies for the STFT. This will be evaluated via test cases showing that the correct shape is achieved within some tolerance, as well as through your spectrogram plots *[1 pt]*
    2. We have generated a chord 🎵 (e.g. multiple notes of different frequencies) that is repeating over time. First load the chord (`assignment1_chord.wav`, at a sample rate of $16,000$Hz). Your goal is to carefully select **two pairs of window and hop sizes** to use in your STFT function such that you produce two spectrogram plots: (1) with high temporal resolution, where you can identify how many repeated chords there are, and (2) with strong frequency resolution, where you can identify the frequencies of the notes present. This will be evaluated via your visual (spectrogram evidence) that supports your answers, and your answers themselves (within some tolerance). *[0.5 each, totals to 1 pt]*

    *Note:* If you are *not* able to get your STFT function working, you may then use `librosa.stft` to proceed with the second part of this section. **You will not receive credit for the STFT portion, but are eligible for points on the second section.**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### STFT Implementation *[1 pt]*
    """)
    return


@app.cell
def _(np, signal):
    # TODO : Write a function for a basic STFT, following the function def below. [1 pt]
    # DO NOT USE LIBROSA, but you can use numpy :)
    def simple_stft(x, frame_len, hop_len, window_type='boxcar'):
        """
        Computes the Short-Time Fourier Transform (STFT) of a 1D signal.

        Before computing the STFT friends, be sure to include:
        - padding to prevent information loss
        - windowing


        Parameters:
        -----------
            x : numpy.ndarray
                Input signal, a 1D array.
            frame_len :  int
                Length of each frame (window size).
            hop_len : int
                Hop length between consecutive frames.
            window_type : str
                Type of window e.g. "hann", "boxcar".

        Returns:
        --------
        stft_result : numpy.ndarray
            A 2D array (n_freqs, n_frames) where each row corresponds to the real,
            non-negative frequency components of a frame.

        """
        N = len(x)
        n_frames = 1 + int(np.ceil((N - frame_len) / hop_len))
        padded_len = (n_frames - 1) * hop_len + frame_len
        x_padded = np.pad(x, (0, max(0, padded_len - N)))  # compute number of frames needed
        w = signal.get_window(window_type, frame_len)  # total length after padding to fit last frame
        n_freqs = frame_len // 2 + 1  # zero-pad signal at the end if needed
        stft_result = np.zeros((n_freqs, n_frames), dtype=np.complex64)
        for i in range(n_frames):  #get window
            start = i * hop_len
            frame = x_padded[start:start + frame_len]
            frame = frame * w  # number of frequency bins for rFFT (real FFT)
            stft_result[:, i] = np.fft.rfft(frame)  # initialize STFT matrix
        return stft_result  # starting index of the current frame  # extract frame of length frame_len  # apply window to reduce spectral leakage  # compute real FFT of the frame and store in STFT

    return (simple_stft,)


@app.cell
def _(IPython):
    # TODO : Test out loading and listening to the repeating chord audio
    IPython.display.Audio('assignment1_chord.wav', rate=16000)
    return


@app.cell
def _(librosa, np, plt, sr_7):
    def plot_spec(stft, hop_length, title=None):
        """
        Plot the magnitude spectrogram of a signal.

        Parameters
        ----------
        stft : np.ndarray
            Magnitude spectrogram.
        hop_length : int
            Hop length between consecutive frames.

        Returns
        ----------
        None, plots the spectrogram.
        """
        log_spec = librosa.amplitude_to_db(np.abs(stft), ref=np.max)
        librosa.display.specshow(log_spec, y_axis='log', sr=sr_7, hop_length=hop_length, x_axis='time')
        plt.title(title)
        return plt.gcf()

    return (plot_spec,)


@app.cell
def _(librosa, plot_spec, simple_stft):
    sr_8 = 16000
    x_1, rate = librosa.load('assignment1_chord.wav', sr=sr_8)
    _stft = simple_stft(x_1, 1024, 128, window_type='hann')
    _plot = plot_spec(_stft, 128, title='STFT of Chord')
    print(f'Frequency bins: expected 513, got {_stft.shape[0]}')
    print(f'Time frames: expected 368, got {_stft.shape[1]}')
    _plot
    return (x_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### (1) Temporally-resolved spectrogram

    TODO : Use your STFT function and the `plot_spec` function to select a window and hop size that allows you to clearly visualize how many times the chord is repeated.
    """)
    return


@app.cell
def _(plot_spec, simple_stft, x_1):
    _hop_size = 10
    _window_type = 'hann'
    _frame_size = 512
    _stft = simple_stft(x_1, _frame_size, _hop_size, window_type=_window_type)
    plot_spec(_stft, _hop_size, title='STFT of Chord (To Count Repetitions)')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### (2) Frequency-resolved spectrogram

    TODO : Use your STFT function and the `plot_spec` function to select a window and hop size that allows you to clearly visualize the frequency components of the chord.
    """)
    return


@app.cell
def _(plot_spec, simple_stft, x_1):
    _hop_size = 10
    _window_type = 'hann'
    _frame_size = 2500
    _stft = simple_stft(x_1, _frame_size, _hop_size, window_type=_window_type)
    plot_spec(_stft, _hop_size, title='STFT of Chord (To Count Repetitions)')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### TODO: Answer these questions using your spectrogram plots above *[1pt]*:

    For full-credit here, ensure that you have visual spectrogram evidence shown above to support your responses.

    1. How many times does the chord repeat? *[0.5 pt]*
    2. How many notes are present in the chord and what are their frequencies? (Note this will be evaluated within some Hz tolerance) *[0.5 pt]*
    """)
    return


@app.cell
def _():
    #1. The chord is repeated 12 times.
    #2. There are three notes present in the chord and their frequencies are approximately 800, 900, and 1000 Hz.
    return


if __name__ == "__main__":
    app.run()
