import numpy as np
import h5py


def dump_to_libsvm_format(file_name, art_mat, train_mat):
    f = open(file_name, "w")
    for mat_idx in range(art_mat.shape[0]):
        f.write(str(cat_mat[mat_idx][0]))
        f.write(" ")
        for col_idx in range(art_mat.shape[1]):
            f.write(str(col_idx + 1))
            f.write(":")
            f.write(str(art_mat[mat_idx][col_idx]))
            f.write(" ")
        f.write("\n")
    f.close()


if __name__ == "__main__":

    file = h5py.File('article_mat.h5', 'r')
    art_mat = file['art_mat'][:]
    cat_mat = file['cat_mat'][:]
    id_mat  = file['id_mat' ][:]
    file.close()

    choice = np.random.choice(art_mat.shape[0], art_mat.shape[0] // 2, replace=False)
    mask = np.zeros(art_mat.shape[0], np.bool)
    mask[choice] = 1
    train_art_mat = art_mat[mask]
    train_cat_mat = cat_mat[mask]
    train_cat_mat = train_cat_mat.reshape(train_cat_mat.shape[0])
    train_id_mat = id_mat[mask]

    mask = np.ones(art_mat.shape[0], np.bool)
    mask[choice] = 0
    test_art_mat = art_mat[mask]
    test_cat_mat = cat_mat[mask]
    test_cat_mat = test_cat_mat.reshape(test_cat_mat.shape[0])
    test_id_mat = id_mat[mask]

    dump_to_libsvm_format("libsvm_train.txt", train_art_mat, train_cat_mat)
    dump_to_libsvm_format("libsvm_test.txt", test_art_mat, test_cat_mat)