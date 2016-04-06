
.. _trylock-functions:

=====================
The trylock Functions
=====================

There are functions that try to acquire a lock only once and immediately return a value telling about success or failure to acquire the lock. They can be used if you need no access
to the data protected with the lock when some other thread is holding the lock. You should acquire the lock later if you then need access to the data protected with the lock.

``spin_trylock()`` does not spin but returns non-zero if it acquires the spinlock on the first try or 0 if not. This function can be used in all contexts like ``spin_lock``: you
must have disabled the contexts that might interrupt you and acquire the spin lock.

``mutex_trylock()`` does not suspend your task but returns non-zero if it could lock the mutex on the first try or 0 if not. This function cannot be safely used in hardware or
software interrupt contexts despite not sleeping.
