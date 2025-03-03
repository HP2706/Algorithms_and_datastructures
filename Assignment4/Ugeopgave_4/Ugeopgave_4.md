# Algoritmer og Datastrukturer (NDAA04010U) Ugeopgave 4

Københavns Universitet

2025

## 1 Dynamisk programmering

En stigende delsekvens af en tabel A, der indeholder heltal A[1], . . . , A[n], er en delmængde af indekser 1 ≤ i1 < i2 < · · · < ik ≤ n s˚aledes at A[i1] < A[i2] < · · · < A[ik]. Længden af delsekvensen er antal indekser, k. En ikke-aftagende delsekvens defineres p˚a samme m˚ade bortset fra at kravet er A[i1] ≤ A[i2] ≤ · · · ≤ A[ik]. Betragt følgende funktion, i pseudo-kode notationen fra CLRS, hvor input A er en tabel af heltal.

MaximumMystery(A, n)

```
1 let r[1 . . . n] be a new array
2 r[1] = 1
3 for j = 2 to n
4 q = 1
5 for i = 1 to j − 1
6 if not A[j] < A[i]
7 q = max(q, r[i] + 1)
8 r[j] = q
9 return max1≤ℓ≤n r[ℓ]
```
Hvad beregner proceduren MaximumMystery? Vælg præcis ´et svar og beskriv hvordan du kom frem til det. Formul´er en invariant for den ydre løkke som en del af dit svar.

- 1. Indekserne i en længste stigende delsekvens.
- 2. Indekserne i en længste ikke-aftagende delsekvens.
- 3. Længden af en længste stigende delsekvens.
- 4. Længden af en længste ikke-aftagende delsekvens.

### 2 Huffman koder

Vi betragter algoritmen til konstruktion af Huffman koder i CLRS sektion 15.3.

a) Tegn Huffman træet som algoritmen beregner for alfabetet C = {a, b, c, d, e} med frekvenser fa = 5, fb = 8, fc = 3, fd = 7, fe = 1. Det er ikke nødvendigt at angive labels (0 og 1) p˚a kanterne, men angiv frekvenser i blade s˚avel som indre knuder (se eksempel i CLRS figur 15.5).

### 3 Mere dynamisk programmering

Vi et givet en liste x0, x1, . . . , xn med n positive heltal. Betragt følgende rekursive definition af værdier mi,j , hvor 1 ≤ i ≤ j ≤ n:

$$m_{i,j} = \begin{cases} 1 \text{ hvis } i = j\\ \max\{m_{i,k} + m_{k+1,j} + x_{i-1}x_kx_j \mid i \le k < j\} \text{ hvis } i < j \end{cases}$$

En rekursiv algoritme der direkte følger rekursionsligningen, uden at gemme beregnede værdier, bruger tid O(ti,j ) til at beregne mi,j , hvor

$$t_{i,j} = \begin{cases} 1 \text{ hvis } i = j\\ 1 + \sum_{k=i}^{j-1} t_{i,k} + t_{k+1,j} \text{ hvis } i < j \end{cases}$$

a) Argument´er for at ti,j ≥ 2 j−i+1 − 1. Brug gerne induktion i ℓ = j − i.

b) Forklar, gerne med pseudokode, hvordan dynamisk programmering kan bruges til effektivt at beregne mi,j for alle 1 ≤ i ≤ j ≤ n. Analys´er plads og køretid for algoritmen, i store-O notation, som funktion af n.

### 4 Gr˚adige algoritmer

Vi betragter igen MaxProduct problemet fra Ugeopgave 2:

Givet en liste af tal x1, . . . , xn ∈ R (kan være b˚ade positive og negative), find en delmængde I ∗ ⊆ {1, . . . , n} hvor produktet Q i∈I ∗ xi er s˚a stort som muligt, dvs. for alle mængder I ⊆ {1, . . . , n} skal gælde at Q i∈I xi ≤ Q i∈I ∗ xi .

Eksempel. P˚a input x1 = −4, x2 = −0.5, x3 = 0.5, x4 = 0.5, x5 = 1.5, x6 = 6 kan vi vælge I = {5, 6} og f˚a et produkt p˚a 1.5 · 6 = 9, men et bedre valg er I = {1, 2, 5, 6} som giver produktet ( Q −4) · (−0.5) · 1.5 · 6 = 18. Den tomme mængde I = ∅ giver per definition i∈∅ xi = 1.

Et mulig tilgang til at løse MaxProdukt er at gr˚adigt føje elementer til I, ´et ad gangen. Antag at input er sorteret s˚aledes at x1 ≤ x2 ≤ · · · ≤ xn.

a) Argument´er for at for en optimal løsning I ∗ vil der altid vil være et lige antal elementer i mængden I ∗ − = {i ∈ I ∗ | xi < 0}, dvs. |I ∗ −| er deleligt med 2.

b) Foresl˚a en effektiv algoritme til at finde en optimal løsning I ∗ . Argument´er for korrekthed og køretid. Der lægges vægt p˚a, at argumentationen er klar og koncis. (Det er ikke et krav at argumentere via "greedy choice property" og "optimal substructure".)