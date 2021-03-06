.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ecryptfs/crypto.c

.. _`decrypt`:

DECRYPT
=======

.. c:function::  DECRYPT()

    Linux filesystem encryption layer

.. _`decrypt.description`:

Description
-----------

Copyright (C) 1997-2004 Erez Zadok
Copyright (C) 2001-2004 Stony Brook University
Copyright (C) 2004-2007 International Business Machines Corp.
Author(s): Michael A. Halcrow <mahalcro@us.ibm.com>
Michael C. Thompson <mcthomps@us.ibm.com>

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License as
published by the Free Software Foundation; either version 2 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
02111-1307, USA.

.. _`ecryptfs_from_hex`:

ecryptfs_from_hex
=================

.. c:function:: void ecryptfs_from_hex(char *dst, char *src, int dst_size)

    :param dst:
        Buffer to take the bytes from src hex; must be at least of
        size (src_size / 2)
    :type dst: char \*

    :param src:
        Buffer to be converted from a hex string representation to raw value
    :type src: char \*

    :param dst_size:
        size of dst buffer, or number of hex characters pairs to convert
    :type dst_size: int

.. _`ecryptfs_calculate_md5`:

ecryptfs_calculate_md5
======================

.. c:function:: int ecryptfs_calculate_md5(char *dst, struct ecryptfs_crypt_stat *crypt_stat, char *src, int len)

    calculates the md5 of \ ``src``\ 

    :param dst:
        Pointer to 16 bytes of allocated memory
    :type dst: char \*

    :param crypt_stat:
        Pointer to crypt_stat struct for the current inode
    :type crypt_stat: struct ecryptfs_crypt_stat \*

    :param src:
        Data to be md5'd
    :type src: char \*

    :param len:
        Length of \ ``src``\ 
    :type len: int

.. _`ecryptfs_calculate_md5.description`:

Description
-----------

Uses the allocated crypto context that crypt_stat references to
generate the MD5 sum of the contents of src.

.. _`ecryptfs_derive_iv`:

ecryptfs_derive_iv
==================

.. c:function:: int ecryptfs_derive_iv(char *iv, struct ecryptfs_crypt_stat *crypt_stat, loff_t offset)

    :param iv:
        destination for the derived iv vale
    :type iv: char \*

    :param crypt_stat:
        Pointer to crypt_stat struct for the current inode
    :type crypt_stat: struct ecryptfs_crypt_stat \*

    :param offset:
        Offset of the extent whose IV we are to derive
    :type offset: loff_t

.. _`ecryptfs_derive_iv.description`:

Description
-----------

Generate the initialization vector from the given root IV and page
offset.

Returns zero on success; non-zero on error.

.. _`ecryptfs_init_crypt_stat`:

ecryptfs_init_crypt_stat
========================

.. c:function:: int ecryptfs_init_crypt_stat(struct ecryptfs_crypt_stat *crypt_stat)

    :param crypt_stat:
        Pointer to the crypt_stat struct to initialize.
    :type crypt_stat: struct ecryptfs_crypt_stat \*

.. _`ecryptfs_init_crypt_stat.description`:

Description
-----------

Initialize the crypt_stat structure.

.. _`ecryptfs_destroy_crypt_stat`:

ecryptfs_destroy_crypt_stat
===========================

.. c:function:: void ecryptfs_destroy_crypt_stat(struct ecryptfs_crypt_stat *crypt_stat)

    :param crypt_stat:
        Pointer to the crypt_stat struct to initialize.
    :type crypt_stat: struct ecryptfs_crypt_stat \*

.. _`ecryptfs_destroy_crypt_stat.description`:

Description
-----------

Releases all memory associated with a crypt_stat struct.

.. _`virt_to_scatterlist`:

virt_to_scatterlist
===================

.. c:function:: int virt_to_scatterlist(const void *addr, int size, struct scatterlist *sg, int sg_size)

    :param addr:
        Virtual address
    :type addr: const void \*

    :param size:
        Size of data; should be an even multiple of the block size
    :type size: int

    :param sg:
        Pointer to scatterlist array; set to NULL to obtain only
        the number of scatterlist structs required in array
    :type sg: struct scatterlist \*

    :param sg_size:
        Max array size
    :type sg_size: int

.. _`virt_to_scatterlist.description`:

Description
-----------

Fills in a scatterlist array with page references for a passed
virtual address.

Returns the number of scatterlist structs in array used

.. _`crypt_scatterlist`:

crypt_scatterlist
=================

.. c:function:: int crypt_scatterlist(struct ecryptfs_crypt_stat *crypt_stat, struct scatterlist *dst_sg, struct scatterlist *src_sg, int size, unsigned char *iv, int op)

    :param crypt_stat:
        Pointer to the crypt_stat struct to initialize.
    :type crypt_stat: struct ecryptfs_crypt_stat \*

    :param dst_sg:
        Destination of the data after performing the crypto operation
    :type dst_sg: struct scatterlist \*

    :param src_sg:
        Data to be encrypted or decrypted
    :type src_sg: struct scatterlist \*

    :param size:
        Length of data
    :type size: int

    :param iv:
        IV to use
    :type iv: unsigned char \*

    :param op:
        ENCRYPT or DECRYPT to indicate the desired operation
    :type op: int

.. _`crypt_scatterlist.description`:

Description
-----------

Returns the number of bytes encrypted or decrypted; negative value on error

.. _`lower_offset_for_page`:

lower_offset_for_page
=====================

.. c:function:: loff_t lower_offset_for_page(struct ecryptfs_crypt_stat *crypt_stat, struct page *page)

    :param crypt_stat:
        *undescribed*
    :type crypt_stat: struct ecryptfs_crypt_stat \*

    :param page:
        *undescribed*
    :type page: struct page \*

.. _`lower_offset_for_page.description`:

Description
-----------

Convert an eCryptfs page index into a lower byte offset

.. _`crypt_extent`:

crypt_extent
============

.. c:function:: int crypt_extent(struct ecryptfs_crypt_stat *crypt_stat, struct page *dst_page, struct page *src_page, unsigned long extent_offset, int op)

    :param crypt_stat:
        crypt_stat containing cryptographic context for the
        encryption operation
    :type crypt_stat: struct ecryptfs_crypt_stat \*

    :param dst_page:
        The page to write the result into
    :type dst_page: struct page \*

    :param src_page:
        The page to read from
    :type src_page: struct page \*

    :param extent_offset:
        Page extent offset for use in generating IV
    :type extent_offset: unsigned long

    :param op:
        ENCRYPT or DECRYPT to indicate the desired operation
    :type op: int

.. _`crypt_extent.description`:

Description
-----------

Encrypts or decrypts one extent of data.

Return zero on success; non-zero otherwise

.. _`ecryptfs_encrypt_page`:

ecryptfs_encrypt_page
=====================

.. c:function:: int ecryptfs_encrypt_page(struct page *page)

    :param page:
        Page mapped from the eCryptfs inode for the file; contains
        decrypted content that needs to be encrypted (to a temporary
        page; not in place) and written out to the lower file
    :type page: struct page \*

.. _`ecryptfs_encrypt_page.description`:

Description
-----------

Encrypt an eCryptfs page. This is done on a per-extent basis. Note
that eCryptfs pages may straddle the lower pages -- for instance,
if the file was created on a machine with an 8K page size
(resulting in an 8K header), and then the file is copied onto a
host with a 32K page size, then when reading page 0 of the eCryptfs
file, 24K of page 0 of the lower file will be read and decrypted,
and then 8K of page 1 of the lower file will be read and decrypted.

Returns zero on success; negative on error

.. _`ecryptfs_decrypt_page`:

ecryptfs_decrypt_page
=====================

.. c:function:: int ecryptfs_decrypt_page(struct page *page)

    :param page:
        Page mapped from the eCryptfs inode for the file; data read
        and decrypted from the lower file will be written into this
        page
    :type page: struct page \*

.. _`ecryptfs_decrypt_page.description`:

Description
-----------

Decrypt an eCryptfs page. This is done on a per-extent basis. Note
that eCryptfs pages may straddle the lower pages -- for instance,
if the file was created on a machine with an 8K page size
(resulting in an 8K header), and then the file is copied onto a
host with a 32K page size, then when reading page 0 of the eCryptfs
file, 24K of page 0 of the lower file will be read and decrypted,
and then 8K of page 1 of the lower file will be read and decrypted.

Returns zero on success; negative on error

.. _`ecryptfs_init_crypt_ctx`:

ecryptfs_init_crypt_ctx
=======================

.. c:function:: int ecryptfs_init_crypt_ctx(struct ecryptfs_crypt_stat *crypt_stat)

    :param crypt_stat:
        Uninitialized crypt stats structure
    :type crypt_stat: struct ecryptfs_crypt_stat \*

.. _`ecryptfs_init_crypt_ctx.description`:

Description
-----------

Initialize the crypto context.

.. _`ecryptfs_init_crypt_ctx.todo`:

TODO
----

Performance: Keep a cache of initialized cipher contexts;
only init if needed

.. _`ecryptfs_compute_root_iv`:

ecryptfs_compute_root_iv
========================

.. c:function:: int ecryptfs_compute_root_iv(struct ecryptfs_crypt_stat *crypt_stat)

    \ ``crypt_stats``\ 

    :param crypt_stat:
        *undescribed*
    :type crypt_stat: struct ecryptfs_crypt_stat \*

.. _`ecryptfs_compute_root_iv.description`:

Description
-----------

On error, sets the root IV to all 0's.

.. _`ecryptfs_copy_mount_wide_flags_to_inode_flags`:

ecryptfs_copy_mount_wide_flags_to_inode_flags
=============================================

.. c:function:: void ecryptfs_copy_mount_wide_flags_to_inode_flags(struct ecryptfs_crypt_stat *crypt_stat, struct ecryptfs_mount_crypt_stat *mount_crypt_stat)

    :param crypt_stat:
        The inode's cryptographic context
    :type crypt_stat: struct ecryptfs_crypt_stat \*

    :param mount_crypt_stat:
        The mount point's cryptographic context
    :type mount_crypt_stat: struct ecryptfs_mount_crypt_stat \*

.. _`ecryptfs_copy_mount_wide_flags_to_inode_flags.description`:

Description
-----------

This function propagates the mount-wide flags to individual inode
flags.

.. _`ecryptfs_set_default_crypt_stat_vals`:

ecryptfs_set_default_crypt_stat_vals
====================================

.. c:function:: void ecryptfs_set_default_crypt_stat_vals(struct ecryptfs_crypt_stat *crypt_stat, struct ecryptfs_mount_crypt_stat *mount_crypt_stat)

    :param crypt_stat:
        The inode's cryptographic context
    :type crypt_stat: struct ecryptfs_crypt_stat \*

    :param mount_crypt_stat:
        The mount point's cryptographic context
    :type mount_crypt_stat: struct ecryptfs_mount_crypt_stat \*

.. _`ecryptfs_set_default_crypt_stat_vals.description`:

Description
-----------

Default values in the event that policy does not override them.

.. _`ecryptfs_new_file_context`:

ecryptfs_new_file_context
=========================

.. c:function:: int ecryptfs_new_file_context(struct inode *ecryptfs_inode)

    :param ecryptfs_inode:
        The eCryptfs inode
    :type ecryptfs_inode: struct inode \*

.. _`ecryptfs_new_file_context.description`:

Description
-----------

If the crypto context for the file has not yet been established,
this is where we do that.  Establishing a new crypto context

.. _`ecryptfs_new_file_context.involves-the-following-decisions`:

involves the following decisions
--------------------------------

- What cipher to use?
- What set of authentication tokens to use?
Here we just worry about getting enough information into the
authentication tokens so that we know that they are available.
We associate the available authentication tokens with the new file
via the set of signatures in the crypt_stat struct.  Later, when
the headers are actually written out, we may again defer to
userspace to perform the encryption of the session key; for the
foreseeable future, this will be the case with public key packets.

Returns zero on success; non-zero otherwise

.. _`ecryptfs_validate_marker`:

ecryptfs_validate_marker
========================

.. c:function:: int ecryptfs_validate_marker(char *data)

    check for the ecryptfs marker

    :param data:
        The data block in which to check
    :type data: char \*

.. _`ecryptfs_validate_marker.description`:

Description
-----------

Returns zero if marker found; -EINVAL if not found

.. _`ecryptfs_process_flags`:

ecryptfs_process_flags
======================

.. c:function:: int ecryptfs_process_flags(struct ecryptfs_crypt_stat *crypt_stat, char *page_virt, int *bytes_read)

    :param crypt_stat:
        The cryptographic context
    :type crypt_stat: struct ecryptfs_crypt_stat \*

    :param page_virt:
        Source data to be parsed
    :type page_virt: char \*

    :param bytes_read:
        Updated with the number of bytes read
    :type bytes_read: int \*

.. _`ecryptfs_process_flags.description`:

Description
-----------

Returns zero on success; non-zero if the flag set is invalid

.. _`write_ecryptfs_marker`:

write_ecryptfs_marker
=====================

.. c:function:: void write_ecryptfs_marker(char *page_virt, size_t *written)

    :param page_virt:
        The pointer to in a page to begin writing the marker
    :type page_virt: char \*

    :param written:
        Number of bytes written
    :type written: size_t \*

.. _`write_ecryptfs_marker.description`:

Description
-----------

Marker = 0x3c81b7f5

.. _`ecryptfs_code_for_cipher_string`:

ecryptfs_code_for_cipher_string
===============================

.. c:function:: u8 ecryptfs_code_for_cipher_string(char *cipher_name, size_t key_bytes)

    :param cipher_name:
        The string alias for the cipher
    :type cipher_name: char \*

    :param key_bytes:
        Length of key in bytes; used for AES code selection
    :type key_bytes: size_t

.. _`ecryptfs_code_for_cipher_string.description`:

Description
-----------

Returns zero on no match, or the cipher code on match

.. _`ecryptfs_cipher_code_to_string`:

ecryptfs_cipher_code_to_string
==============================

.. c:function:: int ecryptfs_cipher_code_to_string(char *str, u8 cipher_code)

    :param str:
        Destination to write out the cipher name
    :type str: char \*

    :param cipher_code:
        The code to convert to cipher name string
    :type cipher_code: u8

.. _`ecryptfs_cipher_code_to_string.description`:

Description
-----------

Returns zero on success

.. _`ecryptfs_write_headers_virt`:

ecryptfs_write_headers_virt
===========================

.. c:function:: int ecryptfs_write_headers_virt(char *page_virt, size_t max, size_t *size, struct ecryptfs_crypt_stat *crypt_stat, struct dentry *ecryptfs_dentry)

    :param page_virt:
        The virtual address to write the headers to
    :type page_virt: char \*

    :param max:
        The size of memory allocated at page_virt
    :type max: size_t

    :param size:
        Set to the number of bytes written by this function
    :type size: size_t \*

    :param crypt_stat:
        The cryptographic context
    :type crypt_stat: struct ecryptfs_crypt_stat \*

    :param ecryptfs_dentry:
        The eCryptfs dentry
    :type ecryptfs_dentry: struct dentry \*

.. _`ecryptfs_write_headers_virt.format-version`:

Format version
--------------

1

.. _`ecryptfs_write_headers_virt.header-extent`:

Header Extent
-------------

Octets 0-7:        Unencrypted file size (big-endian)
Octets 8-15:       eCryptfs special marker
Octets 16-19:      Flags

.. _`ecryptfs_write_headers_virt.octet-16`:

Octet 16
--------

File format version number (between 0 and 255)
Octets 17-18:     Reserved

.. _`ecryptfs_write_headers_virt.octet-19`:

Octet 19
--------

Bit 1 (lsb): Reserved
Bit 2: Encrypted?
Bits 3-8: Reserved
Octets 20-23:      Header extent size (big-endian)
Octets 24-25:      Number of header extents at front of file
(big-endian)

.. _`ecryptfs_write_headers_virt.octet--26`:

Octet  26
---------

Begin RFC 2440 authentication token packet set

.. _`ecryptfs_write_headers_virt.data-extent-0`:

Data Extent 0
-------------

Lower data (CBC encrypted)

.. _`ecryptfs_write_headers_virt.data-extent-1`:

Data Extent 1
-------------

Lower data (CBC encrypted)
...

Returns zero on success

.. _`ecryptfs_write_metadata`:

ecryptfs_write_metadata
=======================

.. c:function:: int ecryptfs_write_metadata(struct dentry *ecryptfs_dentry, struct inode *ecryptfs_inode)

    :param ecryptfs_dentry:
        The eCryptfs dentry, which should be negative
    :type ecryptfs_dentry: struct dentry \*

    :param ecryptfs_inode:
        The newly created eCryptfs inode
    :type ecryptfs_inode: struct inode \*

.. _`ecryptfs_write_metadata.description`:

Description
-----------

Write the file headers out.  This will likely involve a userspace
callout, in which the session key is encrypted with one or more
public keys and/or the passphrase necessary to do the encryption is
retrieved via a prompt.  Exactly what happens at this point should
be policy-dependent.

Returns zero on success; non-zero on error

.. _`set_default_header_data`:

set_default_header_data
=======================

.. c:function:: void set_default_header_data(struct ecryptfs_crypt_stat *crypt_stat)

    :param crypt_stat:
        The cryptographic context
    :type crypt_stat: struct ecryptfs_crypt_stat \*

.. _`set_default_header_data.description`:

Description
-----------

For version 0 file format; this function is only for backwards
compatibility for files created with the prior versions of
eCryptfs.

.. _`ecryptfs_read_headers_virt`:

ecryptfs_read_headers_virt
==========================

.. c:function:: int ecryptfs_read_headers_virt(char *page_virt, struct ecryptfs_crypt_stat *crypt_stat, struct dentry *ecryptfs_dentry, int validate_header_size)

    :param page_virt:
        The virtual address into which to read the headers
    :type page_virt: char \*

    :param crypt_stat:
        The cryptographic context
    :type crypt_stat: struct ecryptfs_crypt_stat \*

    :param ecryptfs_dentry:
        The eCryptfs dentry
    :type ecryptfs_dentry: struct dentry \*

    :param validate_header_size:
        Whether to validate the header size while reading
    :type validate_header_size: int

.. _`ecryptfs_read_headers_virt.description`:

Description
-----------

Read/parse the header data. The header format is detailed in the
comment block for the \ :c:func:`ecryptfs_write_headers_virt`\  function.

Returns zero on success

.. _`ecryptfs_read_xattr_region`:

ecryptfs_read_xattr_region
==========================

.. c:function:: int ecryptfs_read_xattr_region(char *page_virt, struct inode *ecryptfs_inode)

    :param page_virt:
        The vitual address into which to read the xattr data
    :type page_virt: char \*

    :param ecryptfs_inode:
        The eCryptfs inode
    :type ecryptfs_inode: struct inode \*

.. _`ecryptfs_read_xattr_region.description`:

Description
-----------

Attempts to read the crypto metadata from the extended attribute
region of the lower file.

Returns zero on success; non-zero on error

.. _`ecryptfs_read_metadata`:

ecryptfs_read_metadata
======================

.. c:function:: int ecryptfs_read_metadata(struct dentry *ecryptfs_dentry)

    :param ecryptfs_dentry:
        *undescribed*
    :type ecryptfs_dentry: struct dentry \*

.. _`ecryptfs_read_metadata.description`:

Description
-----------

Common entry point for reading file metadata. From here, we could
retrieve the header information from the header region of the file,
the xattr region of the file, or some other repository that is
stored separately from the file itself. The current implementation
supports retrieving the metadata information from the file contents
and from the xattr region.

Returns zero if valid headers found and parsed; non-zero otherwise

.. _`ecryptfs_encrypt_filename`:

ecryptfs_encrypt_filename
=========================

.. c:function:: int ecryptfs_encrypt_filename(struct ecryptfs_filename *filename, struct ecryptfs_mount_crypt_stat *mount_crypt_stat)

    encrypt filename

    :param filename:
        *undescribed*
    :type filename: struct ecryptfs_filename \*

    :param mount_crypt_stat:
        *undescribed*
    :type mount_crypt_stat: struct ecryptfs_mount_crypt_stat \*

.. _`ecryptfs_encrypt_filename.description`:

Description
-----------

CBC-encrypts the filename. We do not want to encrypt the same
filename with the same key and IV, which may happen with hard
links, so we prepend random bits to each filename.

Returns zero on success; non-zero otherwise

.. _`ecryptfs_process_key_cipher`:

ecryptfs_process_key_cipher
===========================

.. c:function:: int ecryptfs_process_key_cipher(struct crypto_skcipher **key_tfm, char *cipher_name, size_t *key_size)

    Perform key cipher initialization.

    :param key_tfm:
        Crypto context for key material, set by this function
    :type key_tfm: struct crypto_skcipher \*\*

    :param cipher_name:
        Name of the cipher
    :type cipher_name: char \*

    :param key_size:
        Size of the key in bytes
    :type key_size: size_t \*

.. _`ecryptfs_process_key_cipher.description`:

Description
-----------

Returns zero on success. Any crypto_tfm structs allocated here
should be released by other functions, such as on a superblock put
event, regardless of whether this function succeeds for fails.

.. _`ecryptfs_destroy_crypto`:

ecryptfs_destroy_crypto
=======================

.. c:function:: int ecryptfs_destroy_crypto( void)

    free all cached key_tfms on key_tfm_list

    :param void:
        no arguments
    :type void: 

.. _`ecryptfs_destroy_crypto.description`:

Description
-----------

Called only at module unload time

.. _`ecryptfs_tfm_exists`:

ecryptfs_tfm_exists
===================

.. c:function:: int ecryptfs_tfm_exists(char *cipher_name, struct ecryptfs_key_tfm **key_tfm)

    Search for existing tfm for cipher_name.

    :param cipher_name:
        the name of the cipher to search for
    :type cipher_name: char \*

    :param key_tfm:
        set to corresponding tfm if found
    :type key_tfm: struct ecryptfs_key_tfm \*\*

.. _`ecryptfs_tfm_exists.description`:

Description
-----------

Searches for cached key_tfm matching \ ``cipher_name``\ 
Must be called with \ :c:type:`struct key_tfm_list_mutex <key_tfm_list_mutex>`\  held
Returns 1 if found, with \ ``key_tfm``\  set
Returns 0 if not found, with \ ``key_tfm``\  set to NULL

.. _`ecryptfs_get_tfm_and_mutex_for_cipher_name`:

ecryptfs_get_tfm_and_mutex_for_cipher_name
==========================================

.. c:function:: int ecryptfs_get_tfm_and_mutex_for_cipher_name(struct crypto_skcipher **tfm, struct mutex **tfm_mutex, char *cipher_name)

    :param tfm:
        set to cached tfm found, or new tfm created
    :type tfm: struct crypto_skcipher \*\*

    :param tfm_mutex:
        set to mutex for cached tfm found, or new tfm created
    :type tfm_mutex: struct mutex \*\*

    :param cipher_name:
        the name of the cipher to search for and/or add
    :type cipher_name: char \*

.. _`ecryptfs_get_tfm_and_mutex_for_cipher_name.description`:

Description
-----------

Sets pointers to \ ``tfm``\  & \ ``tfm_mutex``\  matching \ ``cipher_name``\ .
Searches for cached item first, and creates new if not found.
Returns 0 on success, non-zero if adding new cipher failed

.. _`ecryptfs_encode_for_filename`:

ecryptfs_encode_for_filename
============================

.. c:function:: void ecryptfs_encode_for_filename(unsigned char *dst, size_t *dst_size, unsigned char *src, size_t src_size)

    :param dst:
        Destination location for encoded filename
    :type dst: unsigned char \*

    :param dst_size:
        Size of the encoded filename in bytes
    :type dst_size: size_t \*

    :param src:
        Source location for the filename to encode
    :type src: unsigned char \*

    :param src_size:
        Size of the source in bytes
    :type src_size: size_t

.. _`ecryptfs_decode_from_filename`:

ecryptfs_decode_from_filename
=============================

.. c:function:: void ecryptfs_decode_from_filename(unsigned char *dst, size_t *dst_size, const unsigned char *src, size_t src_size)

    :param dst:
        If NULL, this function only sets \ ``dst_size``\  and returns. If
        non-NULL, this function decodes the encoded octets in \ ``src``\ 
        into the memory that \ ``dst``\  points to.
    :type dst: unsigned char \*

    :param dst_size:
        Set to the size of the decoded string.
    :type dst_size: size_t \*

    :param src:
        The encoded set of octets to decode.
    :type src: const unsigned char \*

    :param src_size:
        The size of the encoded set of octets to decode.
    :type src_size: size_t

.. _`ecryptfs_encrypt_and_encode_filename`:

ecryptfs_encrypt_and_encode_filename
====================================

.. c:function:: int ecryptfs_encrypt_and_encode_filename(char **encoded_name, size_t *encoded_name_size, struct ecryptfs_mount_crypt_stat *mount_crypt_stat, const char *name, size_t name_size)

    converts a plaintext file name to cipher text

    :param encoded_name:
        The encypted name
    :type encoded_name: char \*\*

    :param encoded_name_size:
        *undescribed*
    :type encoded_name_size: size_t \*

    :param mount_crypt_stat:
        *undescribed*
    :type mount_crypt_stat: struct ecryptfs_mount_crypt_stat \*

    :param name:
        The plaintext name
    :type name: const char \*

    :param name_size:
        *undescribed*
    :type name_size: size_t

.. _`ecryptfs_encrypt_and_encode_filename.description`:

Description
-----------

Encrypts and encodes a filename into something that constitutes a
valid filename for a filesystem, with printable characters.

We assume that we have a properly initialized crypto context,
pointed to by crypt_stat->tfm.

Returns zero on success; non-zero on otherwise

.. _`ecryptfs_decode_and_decrypt_filename`:

ecryptfs_decode_and_decrypt_filename
====================================

.. c:function:: int ecryptfs_decode_and_decrypt_filename(char **plaintext_name, size_t *plaintext_name_size, struct super_block *sb, const char *name, size_t name_size)

    converts the encoded cipher text name to decoded plaintext

    :param plaintext_name:
        The plaintext name
    :type plaintext_name: char \*\*

    :param plaintext_name_size:
        The plaintext name size
    :type plaintext_name_size: size_t \*

    :param sb:
        *undescribed*
    :type sb: struct super_block \*

    :param name:
        The filename in cipher text
    :type name: const char \*

    :param name_size:
        The cipher text name size
    :type name_size: size_t

.. _`ecryptfs_decode_and_decrypt_filename.description`:

Description
-----------

Decrypts and decodes the filename.

Returns zero on error; non-zero otherwise

.. This file was automatic generated / don't edit.

