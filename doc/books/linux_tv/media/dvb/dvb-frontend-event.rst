
.. _dvb-frontend-event:

===============
frontend events
===============


.. code-block:: c

     struct dvb_frontend_event {
         fe_status_t status;
         struct dvb_frontend_parameters parameters;
     };


