var gulp = require('gulp');
var concat = require('gulp-concat');
 
gulp.task('concat', function() {
  return gulp.src('./*.py')
    .pipe(concat('code.txt'))
    .pipe(gulp.dest('./dist/'));
});
