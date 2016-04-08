
.. _API-snd-info-get-str:

================
snd_info_get_str
================

*man snd_info_get_str(9)*

*4.6.0-rc1*

parse a string token


Synopsis
========

.. c:function:: const char ⋆ snd_info_get_str( char * dest, const char * src, int len )

Arguments
=========

``dest``
    the buffer to store the string token

``src``
    the original string

``len``
    the max. length of token - 1


Description
===========

Parses the original string and copy a token to the given string buffer.


Return
======

The updated pointer of the original string so that it can be used for the next call.
