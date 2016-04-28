.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mode-parse-command-line-for-connector:

=========================================
drm_mode_parse_command_line_for_connector
=========================================

*man drm_mode_parse_command_line_for_connector(9)*

*4.6.0-rc5*

parse command line modeline for connector


Synopsis
========

.. c:function:: bool drm_mode_parse_command_line_for_connector( const char * mode_option, struct drm_connector * connector, struct drm_cmdline_mode * mode )

Arguments
=========

``mode_option``
    optional per connector mode option

``connector``
    connector to parse modeline for

``mode``
    preallocated drm_cmdline_mode structure to fill out


Description
===========

This parses ``mode_option`` command line modeline for modes and options
to configure the connector. If ``mode_option`` is NULL the default
command line modeline in fb_mode_option will be parsed instead.

This uses the same parameters as the fb modedb.c, except for an extra
force-enable, force-enable-digital and force-disable bit at the end:

<xres>x<yres>[M][R][-<bpp>][@<refresh>][i][m][eDd]

The intermediate drm_cmdline_mode structure is required to store
additional options from the command line modline like the
force-enable/disable flag.


Returns
=======

True if a valid modeline has been parsed, false otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
