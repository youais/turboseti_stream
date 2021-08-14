# turboseti_stream

This is a method to get turbo_seti to accept data in a streaming fashion, i.e. straight from memory, instead of reading a Filterbank or HDF5 file from disk. 
This is especially useful for real-time pipelines where data need to be analysed as they are being recorded.

The aim is to integrate this package into a GNU Radio block thus be able to perform SETI searches from a Gnu Radio flowgraph.

## Requirements
- [turbo_seti] (https://github.com/UCBerkeleySETI/turbo_seti)
- [setigen] (https://github.com/bbrzycki/setigen)
- [Gnu Radio] (https://www.gnuradio.org/)

## Example Usage

```
from turboseti_stream import DopplerFinder

clancy = DopplerFinder(filename="DAT_LOG_FILENAME",
                       out_dir="/datax/scratch/turboseti_stream/",
                       source_name="luyten",
                       src_raj=7.456805, 
                       src_dej=5.225785,
                       tstart=59423.2, 
                       tsamp=1, 
                       n_ints_in_file=16,
                       f_start=0,
                       f_stop=1,
                       n_fine_chans=2**20,
                       max_drift=4.0)
 
# Gnu Radio streamed data:
clancy.find_ET(spectra_supplied_by_a_gnu_radio_function)

# Developer unit testing from a Filterbank file or HDF5 file:
clancy.find_ET_from_file("/path-to-synthetic-gnu-radio-data.fil")

