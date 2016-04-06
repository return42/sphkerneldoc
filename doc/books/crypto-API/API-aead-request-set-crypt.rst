
.. _API-aead-request-set-crypt:

======================
aead_request_set_crypt
======================

*man aead_request_set_crypt(9)*

*4.6.0-rc1*

set data buffers


Synopsis
========

.. c:function:: void aead_request_set_crypt( struct aead_request * req, struct scatterlist * src, struct scatterlist * dst, unsigned int cryptlen, u8 * iv )

Arguments
=========

``req``
    request handle

``src``
    source scatter / gather list

``dst``
    destination scatter / gather list

``cryptlen``
    number of bytes to process from ``src``

``iv``
    IV for the cipher operation which must comply with the IV size defined by ``crypto_aead_ivsize``


Description
===========

Setting the source data and destination data scatter / gather lists which hold the associated data concatenated with the plaintext or ciphertext. See below for the authentication
tag.

For encryption, the source is treated as the plaintext and the destination is the ciphertext. For a decryption operation, the use is reversed - the source is the ciphertext and the
destination is the plaintext.

For both src/dst the layout is associated data, plain/cipher text, authentication tag.

The content of the AD in the destination buffer after processing will either be untouched, or it will contain a copy of the AD from the source buffer. In order to ensure that it
always has a copy of the AD, the user must copy the AD over either before or after processing. Of course this is not relevant if the user is doing in-place processing where src ==
dst.

IMPORTANT NOTE AEAD requires an authentication tag (MAC). For decryption, the caller must concatenate the ciphertext followed by the authentication tag and provide the entire data
stream to the decryption operation (i.e. the data length used for the initialization of the scatterlist and the data length for the decryption operation is identical). For
encryption, however, the authentication tag is created while encrypting the data. The destination buffer must hold sufficient space for the ciphertext and the authentication tag
while the encryption invocation must only point to the plaintext data size. The following code snippet illustrates the memory usage buffer = kmalloc(ptbuflen + (enc ? authsize :
0)); sg_init_one( ``sg``, buffer, ptbuflen + (enc ? authsize : 0)); aead_request_set_crypt(req, ``sg``, ``sg``, ptbuflen, iv);
