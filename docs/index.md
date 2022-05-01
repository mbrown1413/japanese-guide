
# MB's Japanese Guide

<style>
/* Hide side navbar */
.col-md-3 {
    display: none !important;
}
.col-md-9 {
    max-width: 100%;
    flex: 0 0 100%;
}

hr {
    border-top: 1px solid #aaa;
}

/* Cards flexbox */
section {
    display: flex;
    flex-flow: row wrap;
}
article {
    padding: 10px;
    margin: 10px;
    flex: 1;
    border: 2px #aaa solid;
    border-radius: 10px;
}
article h2 {
    margin-top: 0.5rem;
}
</style>

<hr>

Here you'll find my personal recommendantions for how to learn Japanese.

<section>

<article>
    <h2><a href="/guide">Step-by-step Guide</a></h2>
    {{ taglines.guide }}
</article>

<article>
    <h2><a href="/resources">Resources</a></h2>
    {{ taglines.resources }}
</article>

<article>
    <h2><a href="/material">Finding Material</a></h2>
    {{ taglines.material }}
</article>

<article>
    <h2><a href="/advice">Advice</a></h2>
    {{ taglines.advice }}
</article>

</section>
