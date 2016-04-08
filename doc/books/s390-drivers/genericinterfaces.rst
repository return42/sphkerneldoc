
.. _genericinterfaces:

==================
Generic interfaces
==================

Some interfaces are available to other drivers that do not necessarily have anything to do with the busses described above, but still are indirectly using basic infrastructure in
the common I/O layer. One example is the support for adapter interrupts.


.. toctree::
    :maxdepth: 1

    API-register-adapter-interrupt
    API-unregister-adapter-interrupt
    API-airq-iv-create
    API-airq-iv-release
    API-airq-iv-alloc
    API-airq-iv-free
    API-airq-iv-scan
