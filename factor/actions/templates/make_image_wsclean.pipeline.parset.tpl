pipeline.steps=[wsclean]

wsclean.control.kind=recipe
wsclean.control.type=executable_args
wsclean.control.opts.executable={{ imagerroot }}/bin/wsclean
wsclean.control.opts.mapfiles_in=[{{ vis_datamap }}, {{ output_datamap }}]
wsclean.control.opts.inputkeys=[msin, imagename]
wsclean.control.opts.arguments=[-name, imagename, -size, {{ imsize }}, {{ imsize }}, -niter, {{ niter }}, -threshold, {{ threshold_jy }}, -pol, I, -weight, briggs, -0.5, -cleanborder, 0, -scale, {{ cell_deg }}, -joinchannels, -channelsout, {{ nchannels }}, -mgain, {{ mgain }}, -gain, {{ gain }}, -j, {{ ncpu }}, -minuv-l, {{ minuv }}, -maxuv-l, {{ maxuv }}, -no-update-model-required, {{ wsclean_wplanes }} {{wsclean_multiscale}} {{mask}} msin]
wsclean.control.opts.max_per_node={{ n_per_node }}