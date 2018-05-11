# FITS Proto
Protocol buffer for the [FITS astronomical data file format][0].

- [The FITS standard can be found here][1].
- [A primer on the FITS message format can be found here][2].
- [NASA's documentation page on FITS can be found here][3].

The intention of the first release of this protobuf will be to more or less
mimic the FITS standard, including some header key-value pairs that are likely
to be redundant for the protobuf format. A future release will seek to optimize
around the capabilities of protobufs while retaining the core *capabilitity*
of, but not necessarily symantic identity with the FITS standard.

[0]: https://en.wikipedia.org/wiki/FITS
[1]: https://fits.gsfc.nasa.gov/standard40/fits_standard40aa.pdf
[2]: https://fits.gsfc.nasa.gov/fits_primer.html
[3]: https://fits.gsfc.nasa.gov/fits_documentation.html
