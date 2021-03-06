import {Entity, model, property, hasMany} from '@loopback/repository';
import {History} from './history.model';
import {State} from './state.model';

@model({settings: {strict: false}})
export class Batch extends Entity {
  @property({
    type: 'number',
    id: true,
    generated: true,
  })
  batch_id?: number;

  @property({
    type: 'string',
    required: true,
  })
  batch_name: string;

  @property({
    type: 'number',
    required: true,
  })
  parent_batch_id: number;

  @property({
    type: 'string',
  })
  description?: string;

  @property({
    type: 'date',
    required: true,
  })
  date_time_start: string;

  @property({
    type: 'date',
    required: true,
  })
  date_time_end: string;

  @hasMany(() => History)
  histories: History[];

  @hasMany(() => State)
  states: State[];
  // Define well-known properties here

  // Indexer property to allow additional data
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  [prop: string]: any;

  constructor(data?: Partial<Batch>) {
    super(data);
  }
}

export interface BatchRelations {
  // describe navigational properties here
}

export type BatchWithRelations = Batch & BatchRelations;
