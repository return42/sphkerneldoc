
.. _API-struct-dvb-frontend-tune-settings:

=================================
struct dvb_frontend_tune_settings
=================================

*man struct dvb_frontend_tune_settings(9)*

*4.6.0-rc1*

parameters to adjust frontend tuning


Synopsis
========

.. code-block:: c

    struct dvb_frontend_tune_settings {
      int min_delay_ms;
      int step_size;
      int max_drift;
    };


Members
=======

min_delay_ms
    minimum delay for tuning, in ms

step_size
    step size between two consecutive frequencies

max_drift
    maximum drift


NOTE
====

step_size is in Hz, for terrestrial/cable or kHz for satellite
