<template>
  <div class="hello">
    <h2>{{ question['question'] }}</h2>
    <p style="font-size: 26px">
      <input type="checkbox" id="answer_a" name="answer_a" v-model="answer_a_selected">
      <label for="answer_a"><span :class="{'blue':question['answer_a_correct']&&checking}" style="margin-right: 12px;">{{
          question['answer_a']
        }}</span>
        <span class="green" v-if="checking&&answer_a_correct">Dobrze</span>
        <span class="red"
              v-if="checking&&!answer_a_correct">Źle</span>
      </label><br>

      <input type="checkbox" id="answer_b" name="answer_b" v-model="answer_b_selected">
      <label for="answer_b"><span :class="{'blue':question['answer_b_correct']&&checking}" style="margin-right: 12px;">{{
          question['answer_b']
        }}</span>
        <span class="green" v-if="checking&&answer_b_correct">Dobrze</span>
        <span class="red"
              v-if="checking&&!answer_b_correct">Źle</span></label><br>

      <input type="checkbox" id="answer_c" name="answer_c" v-model="answer_c_selected">
      <label for="answer_c"><span :class="{'blue':question['answer_c_correct']&&checking}" style="margin-right: 12px;">{{
          question['answer_c']
        }}</span> <span class="green"
                        v-if="checking&&answer_c_correct">Dobrze</span>
        <span class="red"
              v-if="checking&&!answer_c_correct">Źle</span></label><br>

      <input type="checkbox" id="answer_d" name="answer_d" v-model="answer_d_selected">
      <label for="answer_d"><span :class="{'blue':question['answer_d_correct']&&checking}" style="margin-right: 12px;">{{
          question['answer_d']
        }}</span>
        <span class="green" v-if="checking&&answer_d_correct">Dobrze</span>
        <span class="red"
              v-if="checking&&!answer_d_correct">Źle</span></label><br>

    </p>

    <h1 style="color: green" v-if="answer_a_correct&&answer_b_correct&&answer_c_correct&&answer_d_correct">
      Gratulacje</h1>

    <button @click="check" style="font-size: 26px; margin-right: 12px;">Sprawdź</button>
    <br/>
    <button @click="load(-1)" style="font-size: 26px;">Wstecz</button>
    <br/>
    <b style="margin-left: 4px; margin-right: 4px;">{{ i + 1 }}</b><br/>
    <button @click="load(1)" style="font-size: 26px;">Dalej</button>
  </div>
</template>

<script>
const questions = require('../assets/questions.json');

function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    const temp = array[i];
    array[i] = array[j];
    array[j] = temp;
  }
}

export default {
  name: 'HelloWorld',
  data() {
    return {
      question: {},
      answer_a_selected: false,
      answer_b_selected: false,
      answer_c_selected: false,
      answer_d_selected: false,
      answer_a_correct: false,
      answer_b_correct: false,
      answer_c_correct: false,
      answer_d_correct: false,
      checking: false,
      questions,
      i: 0,
      answered_correctly: 0,
      answered: 0
    };
  },
  mounted() {
    shuffleArray(this.questions);
    this.load(0);
  },
  methods: {
    load(direction = 1) {
      this.i = Math.max(this.i + direction, 0);
      this.question = questions[this.i];
      const pairs = [];
      this.answer_a_correct = false;
      this.answer_b_correct = false;
      this.answer_c_correct = false;
      this.answer_d_correct = false;
      this.answer_a_selected = false;
      this.answer_b_selected = false;
      this.answer_c_selected = false;
      this.answer_d_selected = false;
      this.checking = false;
      if (this.i > this.questions.length - 1) {
        alert('Czas na piwo!');
        return;
      }
      pairs.push([this.question['answer_a'], this.question['answer_a_correct']]);
      pairs.push([this.question['answer_b'], this.question['answer_b_correct']]);
      pairs.push([this.question['answer_c'], this.question['answer_c_correct']]);
      pairs.push([this.question['answer_d'], this.question['answer_d_correct']]);
      shuffleArray(pairs);
      this.question['answer_a'] = pairs[0][0];
      this.question['answer_a_correct'] = pairs[0][1];
      this.question['answer_b'] = pairs[1][0];
      this.question['answer_b_correct'] = pairs[1][1];
      this.question['answer_c'] = pairs[2][0];
      this.question['answer_c_correct'] = pairs[2][1];
      this.question['answer_d'] = pairs[3][0];
      this.question['answer_d_correct'] = pairs[3][1];
    },
    check() {
      this.answer_a_correct = this.answer_a_selected === this.question['answer_a_correct'];
      this.answer_b_correct = this.answer_b_selected === this.question['answer_b_correct'];
      this.answer_c_correct = this.answer_c_selected === this.question['answer_c_correct'];
      this.answer_d_correct = this.answer_d_selected === this.question['answer_d_correct'];
      this.checking = true;
      if (this.answer_a_correct &&
          this.answer_b_correct &&
          this.answer_c_correct &&
          this.answer_d_correct) this.answered_correctly++;
      this.answered++;
      document.title = `Fizyka Quiz (${this.answered_correctly}/${this.answered})`;
    },
    next() {
      this.load();
    }
  }
}
</script>

<style>
input[type=checkbox] {
  transform: scale(1.5);
  margin-right: 12px;
}

.green {
  color: green;
}

.red {
  color: red;
}

.blue {
  color: blue;
}
</style>
