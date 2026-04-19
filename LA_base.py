{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "63def45d-1bd0-463b-bdf6-9cf79a69cc1c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1  2  3  4]\n",
      " [ 5  6  7  8]\n",
      " [ 9 10 11 50]\n",
      " [13 14 15 16]]\n",
      "29.086079144497972\n",
      "SVDResult(U=array([[-8.72955339e-02, -7.34386656e-02,  8.37419827e-01,\n",
      "         5.34522484e-01],\n",
      "       [-2.00914540e-01, -3.20394937e-01,  4.62734578e-01,\n",
      "        -8.01783726e-01],\n",
      "       [-8.76754372e-01,  4.78390194e-01, -4.94428269e-02,\n",
      "        -2.07423683e-17],\n",
      "       [-4.28152552e-01, -8.14307479e-01, -2.86635921e-01,\n",
      "         2.67261242e-01]]), S=array([5.96506922e+01, 1.70858583e+01, 1.36688174e+00, 1.02299543e-16]), Vh=array([[-2.43897266e-01, -2.70604702e-01, -2.97312137e-01,\n",
      "        -8.82548986e-01],\n",
      "       [-4.65642328e-01, -5.08353140e-01, -5.51063952e-01,\n",
      "         4.70194458e-01],\n",
      "       [-7.46340860e-01, -4.10306451e-02,  6.64279570e-01,\n",
      "        -4.94567150e-03],\n",
      "       [ 4.08248290e-01, -8.16496581e-01,  4.08248290e-01,\n",
      "         1.08563327e-16]]))\n",
      "[[ 1.27003136  1.40910336  1.54817536  4.59564352]\n",
      " [ 2.92303347  3.24311384  3.5631942  10.57707723]\n",
      " [12.7555844  14.1523567  15.54912899 46.156434  ]\n",
      " [ 6.22903767  6.91113478  7.59323189 22.53994464]]\n",
      "0.0\n"
     ]
    }
   ],
   "source": [
    "#LA_base.py\n",
    "import numpy as np\n",
    "\n",
    "#create matrix\n",
    "A = np.arange(1, 17).reshape(4, 4)\n",
    "A_check = A[2, 3] = 50\n",
    "print(A)\n",
    "\n",
    "#norm\n",
    "A_norm = np.linalg.norm(A[3])\n",
    "print(A_norm)\n",
    "\n",
    "#svd and approximation\n",
    "U, S, Vt = np.linalg.svd(A)\n",
    "k = 1\n",
    "U_k = U[:, :k]\n",
    "D_k = np.diag(S[:k])\n",
    "V_k = Vt[:k, :]\n",
    "rec = U_k @ D_k @ V_k\n",
    "print(res)\n",
    "print(rec)\n",
    "\n",
    "#check\n",
    "A_check_det = np.linalg.det(A - rec)\n",
    "print(A_check_det)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e9c12cae-7f98-4e64-8999-64183c870ca3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
